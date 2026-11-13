import streamlit as st 
import cv2 
import numpy as np
st.title("Колірний сплеск")
uploaded_file = st.file_uploader( "Завантаж фото", type=["jpg", "jpeg", "png"] )
if uploaded_file is not None:
    file_bytes = np.frombuffer(uploaded_file.getvalue(), np.uint8)
img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

if img is None:
    st.error("Не вдалося завантажити фото спрлбуй ще раз")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.image(img, caption="Оригінальне фото")

    color = st.selectbox(
        "Обери колір:",
        ["Червоний", "Зелений", "Синій"]
    )

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    if color == "Червоний":
        low1 = np.array([0, 50, 50])
        high1 = np.array([10, 255, 255])
        low2 = np.array([170, 50, 50])
        high2 = np.array([179, 255, 255])

        mask1 = cv2.inRange(hsv, low1, high1)
        mask2 = cv2.inRange(hsv, low2, high2)
        mask = cv2.bitwise_or(mask1, mask2)

    elif color == "Зелений":
        low = np.array([35, 50, 50])
        high = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, low, high)

    else:
        low = np.array([90, 50, 50])
        high = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, low, high)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

result = np.where(mask[:, :, None] > 0, img, gray)
result = result.astype(np.uint8)

st.subheader("Результат ")
st.image(result, caption="Color Splash")