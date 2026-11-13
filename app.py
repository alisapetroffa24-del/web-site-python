import os
import urllib.parse
import requests
import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

HF_API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
HF_TOKEN = os.getenv("HF_TOKEN")

def generate_image(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed=42"

        response = requests.get(url, timeout=45)

        if response.status_code == 200:
            return response.content, None
        else:
            return None, f"Сервіс тимчасово недоступний: ({response.status_code})"
    except requests.exceptions.Timeout:
        return None,"Time-Out"
    except Exception as e:
        return None, f"Помилка підключення: {e}"


st.title("AI Creative Studio")
st.write("Опишиnm яке зображення хочеш отримати")

prompt = st.text_area("Ваш промпт:")

STYLES = {
    "Без стилю": "",
    "Реалістичний": "high detail, photorealistic, natural lighting",
    "Акварель": "watercolor painting style, soft edges, pastel colors",
    "Мультяшний": "3D animated movie style, vibrant colors, friendly look",
    "Піксель-Арт": "pixel art style, 16-bit retro game aesthetic"
}

styles_choice = st.selectbox("Стилі:", list(STYLES.keys()))

if st.button("Сгенерувати зображення") and prompt:
    final_prompt = prompt + STYLES[styles_choice]

    with st.spinner("AI створює зображення"):
        image_bytes, error = generate_image(final_prompt)

    if error:
        st.error(f"Не вдалося сгенерувати зображення: {error}")
    elif image_bytes:
        st.image(image_bytes, caption=f"Стиль: {styles_choice}", use_container_width=True)
        st.session_state["last_image"] = image_bytes

if "last_image" in st.session_state:
    image = Image.open(BytesIO(st.session_state["last_image"]))
    st.subheader("Фільтри зображення")

filter_choice = st.selectbox(
    "Оберіть фільтр:",
    [
        "Оригінал",
        "Чорно-білий",
        "Розмиття",
        "Різкість",
        "Контури"
    ]
)

if filter_choice == "Чорно-білий":
    image = image.convert("L")

elif filter_choice == "Розмиття":
    image = image.filter(ImageFilter.BLUR)

elif filter_choice == "Різкість":
    image = ImageEnhance.Sharpness(image).enhance(3)

elif filter_choice == "Контури":
    image = image.filter(ImageFilter.CONTOUR)

st.image(image, caption="Оброблене зображення",
         use_container_width=True)
buffer = BytesIO()
image.save(buffer, format="PNG")

st.download_button(
    label="Завантажити",
    data=buffer.getvalue(),
    file_name="ai_result.png",
    mime="image/png"
)