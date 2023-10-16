import numpy as np
import pickle
import pandas as pd 
import streamlit as st
import joblib



pickle_in = open("Scoring02.pkl","rb")
regressor=pickle.load(pickle_in)

def predict_Credit_approval(Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business):
    prediction = regressor.predict([[Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business]])
    return prediction

def main():
    st.title("Прогноз выдачи кредита")
    st.markdown("Учебная модель поможет предсказать одобрение выдачи кредита на основе введенных данных.")
    
    
    
    Gender = st.radio('Ваш пол?(0 - male, 1 - female)', (0, 1)) 
    Sum_issued = st.number_input('Какая сумма выдачи номинала(используйте только цифры)?', step=1, value=0)
    Period  = st.number_input('На какой срок вы хотите взять кредит?(используйте только цифры)?', step=1, value=0) 
    Age = st.slider("Age:", min_value=0, max_value=100, step=1)
    Family_status = st.radio('Каков ваш семеный статус?(0 - Widow/Widower, 1 - Single, 2 - Married, 3 - Divorced)', (0, 1, 2, 3))
    Type_of_client = st.radio('Какой вы клиент?(0 - Новый клиент, 1 - Старый клиент)', (0, 1))    
    Education = st.radio('Какое у вас образование?(0 -  Начал образование, 1 - Непол Сред.образ,  2 - Среднее образование, 3 - Сред.спец.образ-ние, 4 - Высшее образование, 5 - Аспирантура)', (0, 1, 2, 3, 4, 5))
    Type_of_business = st.radio('Какой у вас тип бизнеса?(1 - 1. Карзи истеъмоли/Потребительский кредит, 2 - 2. Истехсолот/Производство, 3 - 6. Хочагии кишлок / Сельское хозяйство, 4 - 3. Хизматрасони/Услуги, 5 - 4. Савдо / Торговля)', (1, 2, 3, 4, 5)) 


    prediction=""
    if st.button("Предсказать"):
        prediction=int(predict_Credit_approval(Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business))
    st.success(f"Предсказание:  {'Кредит одобрен' if prediction[0] == 1 else 'Кредит не одобрен'}")
     
     
 
if __name__ == '__main__':
    main()
     

