import streamlit as st
import joblib
import numpy as np

# Загрузка модели
model = joblib.load('model.pkl')

# Заголовок приложения
st.title("Качество воды")

# Ввод параметров
ph = st.number_input("pH: значение рН воды (от 0 до 14)", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Жесткость (мг/л)", min_value=0.0)
solids = st.number_input("Содержание твердых веществ (млн/долей)", min_value=0.0)
chloramines = st.number_input("Хлорамины (млн/долей)", min_value=0.0)
sulfate = st.number_input("Сульфат (мг/л)", min_value=0.0)
conductivity = st.number_input("Электропроводность", min_value=0.0)
organic_carbon = st.number_input("Органический углерод (млн/долей)", min_value=0.0)
trihalomethanes = st.number_input("Тригалометаны", min_value=0.0)
turbidity = st.number_input("Turbidity", min_value=0.0)

# Кнопка для предсказания
if st.button("Проверить пригодность воды"):
    # Подготовка входных данных для модели
    input_data = np.array(
        [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

    # Получение предсказания
    prediction = model.predict(input_data)

    # Вывод результата
    if prediction[0] == 1:
        st.success("Вода пригодна!")
    else:
        st.error("Вода не пригодна!")
