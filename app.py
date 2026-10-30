import random
import streamlit as st

st.title("Привіттт!")
st.write("Цей сайт створено виключно на Python")

tab1, tab2, tab3 = st.tabs([
    "Про мене", 
    "Мій інструмент", 
    "Гра: Вгадай число"
])

with tab1:
    st.header("Знайомство з мною")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://wikimedia.org")
        
    with col2:
        st.subheader("Привіт, я Аліса!")
        st.write("Я навчаюсь в Малій Комп'ютерній Академії IT STEP та дуже люблю цим займатись.")
    # Продолжение Вкладки 1 (внутри block с col2)
    with st.container():
        st.info("Контакти для зв'язку")
        st.markdown("- E-Mail: t676767@67676")

with tab2:
    st.header("Мій інструмент")
    st.write("Тут буде мій інструмент.")

with tab3:
    st.subheader("Гра: Вгадай число від 1 до 100")
    
    # Ініціалізація загаданого числа в сесії
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    user_guess = st.number_input(
        "Твій варіант:", 
        min_value=1, 
        max_value=100, 
        step=1
    )
    if not st.session_state.game_over:
        if st.button("Перевірити"):
            st.session_state.attempts += 1
            
            if user_guess < st.session_state.secret_number:
                st.info("📈 Загадане число БІЛЬШЕ!")
            elif user_guess > st.session_state.secret_number:
                st.info("📉 Загадане число МЕНШЕ!")
            else:
                st.success(f"🎉 Перемога! Ти вгадав число {st.session_state.secret_number} за {st.session_state.attempts} спроб!")
                st.session_state.game_over = True

    if st.session_state.game_over:
        if st.button("Зіграти спочату"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.rerun()
