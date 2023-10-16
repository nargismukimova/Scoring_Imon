import numpy as np
import pickle
import pandas as pd 
import streamlit as st
import joblib

model_selected = st.radio('What analysis do you want to use', ('KNeighborsClassifier',  'LogisticRegression', 'DecisionTreeClassifier', 'RandomForestClassifier(without options)',  'RandomForestClassifier(with options)', 'Default'))


if model_selected == 'DecisionTreeClassifier':
    pickle_in = open("scoring_imon_ModelTree.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['LogisticRegression', 'Default']:
    pickle_in = open("scoring_imon_LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(with options)':
    pickle_in = open("scoring_imon_Forest(par).pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(without options)':
    pickle_in = open("scoring_imon_Forest.pkl","rb")
    classifier=pickle.load(pickle_in)


def predict_note_authentication(Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business):
    prediction=classifier.predict([[Gender, Sum_issued, Period, Age, Family_status, Type_of_client, Education, Type_of_business]])
    print(prediction)
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


   
     
       result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(Пол, Сумма_выдачи_номинал, Срок, Возраст_полные_года, Family_status, Type_of_client, Education, Tupe_of_business)) 
     #st.success('The output is {}'.format(result))
    st.success('Scoring system result is(1 - Длительность самой долгой единовременной просрочки в течение цикла > 20, 0 - Scoring system result is(1 - Длительность самой долгой единовременной просрочки в течение цикла <= 20) {}'.format(result))
                     
    
    
    
 
if __name__ == '__main__':
    main()
     

