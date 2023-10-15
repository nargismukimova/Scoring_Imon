import pickle
import streamlit as st

file_path = "Scoring02.pkl"  

with open(file_path, "rb") as pickle_in:
    regressor = pickle.load(pickle_in)




def encode_Education(Education):
    Education_mapping = {
        "Высшее образование": 4,
        "Сред.спец.образ-ние": 3,
        "Среднее образование": 2,
        "Непол Сред.образ": 1,
        "Начал образование": 0,
        "Аспирантура": 5
    }
    return Education_mapping.get(Education, 0)

def encode_Type_of_client(Type_of_client):
    Type_of_client_mapping = {
        "Новый клиент": 0,
        "Старый клиент": 1
    }
    return Type_of_client_mapping.get(Type_of_client, 0)

def encode_Type_of_business(Type_of_business):
    Type_of_business_mapping = {
        "Потребительский кредит": 1,
        "Производство": 2,
        "Услуги": 3,
        "Торговля": 4,
        "Сельское хозяйство": 5
    }
    return Type_of_business_mapping.get(Type_of_business, 0)

Family_status_explanation = {
    "Married": 2,
    "Single": 1,
    "Widow/Widower": 0,
    "Divorced": 3
}

def encode_Family_status(Family_status):
    return Family_status_explanation.get(Family_status, 0)

def predict_Credit_approval(Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business):
    Education_encoded = encode_Education(Education)
    Type_of_client_encoded = encode_Type_of_client(Type_of_client)
    Type_of_business_encoded = encode_Type_of_business(Type_of_business)
    Family_status_encoded = encode_Family_status(Family_status)
    
    input_data = [[Gender, Sum_issued, Period, Age, Family_status_encoded, Type_of_client_encoded, Education_encoded, Type_of_business_encoded]]
    
    prediction = regressor.predict(input_data)
    return prediction

def main():
    st.title("Прогноз выдачи кредита")
    st.markdown("Учебная модель поможет предсказать одобрение выдачи кредита на основе введенных данных.")
    
  
    
    Gender_options = ["Мужской", "Женский"]
Gender_selected = st.radio("Пол:", options=Gender_options)


Gender = 0 if Gender_selected == "Мужской" else 1


st.write(f"Выбранный пол: {'Мужской' if Gender == 0 else 'Женский'}")
    
    
    
    Sum_issued = st.number_input("Сумма выдачи кредита:", min_value=0.0, format="%.2f")
    Period = st.number_input("Период:", min_value=0)
    Age = st.slider("Возраст:", min_value=0, max_value=100, step=1)

    Family_status = st.radio("Семейное положение:", options=["Married", "Single", "Widow/Widower", "Divorced"])
    
    Type_of_client = st.radio("Тип клиента:", options=["Новый клиент", "Старый клиент"])

    Education = st.selectbox("Образование:", options=["Высшее образование", "Сред.спец.образ-ние", "Среднее образование", "Непол Сред.образ", "Начал образование", "Аспирантура"])
    Type_of_business = st.selectbox("Тип бизнеса:", options=["Потребительский кредит", "Производство", "Услуги", "Торговля", "Сельское хозяйство"])
    
    if st.button("Предсказать"):
        prediction = regressor.predict_Credit_approval([[Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business]])
        st.success(f"Предсказание: {'Кредит одобрен' if prediction[0] == 1 else 'Кредит не одобрен'}")

if __name__ == '__main__':
    main()