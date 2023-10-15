import pickle
import streamlit as st


with open("Scoring02.pkl", "rb") as pickle_in:  # Замените "ваш_файл.pkl" на имя вашего файла
    classifier = pickle.load(pickle_in)


def encode_education(education):
    education_mapping = {
        "Высшее образование": 4,
        "Сред.спец.образ-ние": 3,
        "Среднее образование": 2,
        "Непол Сред.образ": 1,
        "Начал образование": 0,
        "Аспирантура": 5
    }
    return education_mapping.get(education, 0)

def encode_type_of_client(type_of_client):
    type_of_client_mapping = {
        "Новый клиент": 0,
        "Старый клиент": 1
    }
    return type_of_client_mapping.get(type_of_client, 0)

def encode_type_of_business(type_of_business):
    type_of_business_mapping = {
        "Потребительский кредит": 1,
        "Производство": 2,
        "Услуги": 3,
        "Торговля": 4,
        "Сельское хозяйство": 5
    }
    return type_of_business_mapping.get(type_of_business, 0)


family_status_explanation = {
    "Married": 2,
    "Single": 1,
    "Widow/Widower": 0,
    "Divorced": 3
}

def encode_family_status(family_status):
    return family_status_explanation.get(family_status, 0)

def predict_credit_approval(gender, sum_issued, period, age, family_status, type_of_client, education, type_of_business):
    education_encoded = encode_education(education)
    type_of_client_encoded = encode_type_of_client(type_of_client)
    type_of_business_encoded = encode_type_of_business(type_of_business)
    family_status_encoded = encode_family_status(family_status)
    
    input_data = [[gender, sum_issued, period, age, family_status_encoded, type_of_client_encoded, education_encoded, type_of_business_encoded]]
    
    prediction = classifier.predict(input_data)
    return prediction

def main():
    st.title("Прогноз выдачи кредита")
    st.markdown("Учебная модель поможет предсказать одобрение выдачи кредита на основе введенных данных.")
    
    gender = st.radio("Пол:", options=["Мужской", "Женский"])
    gender = 0 if gender == "Мужской" else 1
    
    sum_issued = st.number_input("Сумма выдачи кредита:", min_value=0.0, format="%.2f")
    period = st.number_input("Период:", min_value=0)
    age = st.slider("Возраст:", min_value=0, max_value=100, step=1)

    
    family_status = st.radio("Семейное положение:", options=["Married", "Single", "Widow/Widower", "Divorced"])
    
    type_of_client = st.radio("Тип клиента:", options=["Новый клиент", "Старый клиент"])

    education = st.selectbox("Образование:", options=["Высшее образование", "Сред.спец.образ-ние", "Среднее образование", "Непол Сред.образ", "Начал образование", "Аспирантура"])
    type_of_business = st.selectbox("Тип бизнеса:", options=["Потребительский кредит", "Производство", "Услуги", "Торговля", "Сельское хозяйство"])
    
    if st.button("Предсказать"):
        prediction = predict_credit_approval(gender, sum_issued, period, age, family_status, type_of_client, education, type_of_business)
        st.success(f"Предсказание: {'Кредит одобрен' if prediction[0] == 1 else 'Кредит не одобрен'}")

if __name__ == '__main__':
    main()