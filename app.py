import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide")

# Load models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(r"C:\Users\anush\OneDrive\Desktop\aicte\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\anush\OneDrive\Desktop\aicte\heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\anush\OneDrive\Desktop\aicte\parkinsons_model.sav", 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreaks System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],  # Fixed missing comma
                           menu_icon='hospital-fill',  # Fixed typo here
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)  # Fixed typo here

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')  # Fixed typo
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Type')  # 0: Typical angina, 1: Atypical angina, 2: Non-anginal pain, 3: Asymptomatic
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol Level')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar')  # 0: < 120 mg/dl, 1: >= 120 mg/dl
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')  # 0: Normal, 1: ST-T wave abnormality, 2: Left ventricular hypertrophy
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')  # 0: No, 1: Yes
    with col1:
        oldpeak = st.text_input('Oldpeak')  # Depression induced by exercise relative to rest
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')  # 0: Upsloping, 1: Flat, 2: Downsloping
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia')  # 3: Normal, 6: Fixed defect, 7: Reversible defect

    heart_diagnosis = ""

    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                float(ca), float(thal)
            ]

            # Make prediction
            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is likely to have heart disease'
            else:
                heart_diagnosis = 'The person is not likely to have heart disease'

            st.success(heart_diagnosis)

        except ValueError:
            st.error("Please enter valid numeric values for all fields.")


# Parkinson's Prediction
if selected == 'Parkinsons Prediction':
    st.title('Parkinson Disorder Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        mdvp_fo = st.text_input('MDVP:Fo (Hz)')
    with col2:
        mdvp_fhi = st.text_input('MDVP:Fhi (Hz)')
    with col3:
        mdvp_flo = st.text_input('MDVP:Flo (Hz)')
    with col4:
        mdvp_jitter = st.text_input('MDVP:Jitter (%)')
    with col5:
        mdvp_jitter_abs = st.text_input('MDVP:Jitter (Abs)')

    with col1:
        mdvp_rap = st.text_input('MDVP:RAP')
    with col2:
        mdvp_ppq = st.text_input('MDVP:PPQ')
    with col3:
        jitter_ddp = st.text_input('Jitter:DDP')
    with col4:
        mdvp_shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        mdvp_shimmer_db = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        shimmer_apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        shimmer_apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        mdvp_apq = st.text_input('MDVP:APQ')
    with col4:
        shimmer_dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')

    with col1:
        hnr = st.text_input('HNR')
    with col2:
        status = st.text_input('Status')  # Healthy = 0, Affected = 1
    with col3:
        rpde = st.text_input('RPDE')
    with col4:
        dfa = st.text_input('DFA')
    with col5:
        spread1 = st.text_input('Spread1')

    with col1:
        spread2 = st.text_input('Spread2')
    with col2:
        d2 = st.text_input('D2')
    with col3:
        ppe = st.text_input('PPE')

    parkinsons_diagnosis = ''
    if st.button('Predict'):
        # Collecting input values
        user_input = [mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp,
                      mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr,
                       rpde, dfa, spread1, spread2, d2, ppe]
        # Processing input to required format (converting to float)
        user_input = [float(x) for x in user_input]  # Handling empty inputs
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person is likely to have parkinson disorder'
        else:
            parkinsons_diagnosis = 'The person is not likely to have a parkinson disorder'

    st.success(parkinsons_diagnosis)
