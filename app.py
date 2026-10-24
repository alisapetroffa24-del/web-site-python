import streamlit as st
st.title("Привіттт!") 
st.write("Цей сайт створено виключно на Python")

tab1, tab2 = st.tabs(["Про мене", "Мій інструмент"])
with tab1: st.header("Знайомство з мною")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://thumb.wikimedia.org/wikipedia/commons/thumb/1/12/Full_image_of_Tung_Tung_Tung_Sahur.png/250px-Full_image_of_Tung_Tung_Tung_Sahur.png?utm_source=ru.wikipedia.org&utm_campaign=parser&utm_content=thumbnail")

with col2:
    st.subheader("Привіт, я Аліса!")
    st.write("Я навчаюсь в Малій Комп'ютерній Академії IT STEP та дуже люблю цим займатися")

    with st.container():
        st.info("Контакти для зв'язку")
        st.markdown("- E-Mail: t676767@67676")
with tab2: st.header("Мій інструмент") 
st.write("Тут буде мій інструмент.")