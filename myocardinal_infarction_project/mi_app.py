import streamlit as st
import joblib
import pandas as pd
import sklearn
# Load the trained model
model = joblib.load('MI_dt_model.pkl')

st.title('Myocardinal Infarction App')

# Input form for user to enter feature values
st.header('Enter Feature Values:')
feature1 = st.number_input('AGE')
feature2 = st.number_input('STENOK_AN')
feature3 = st.number_input('ZSN_AN')
feature4 = st.number_input('S_AD_ORBIT')
feature5 = st.number_input('D_AD_ORBIT')
feature6 = st.number_input('K_SH_POST')
feature7 = st.number_input('ant_im')
feature8 = st.number_input('ROE')
# Add more input fields for other features as needed

# Create a dictionary from user input
user_input = {
    'AGE': [feature1],
    'STENOK_AN': [feature2],
    'ZSN_AN': [feature3],
    'S_AD_ORBIT': [feature4],
    'D_AD_ORBIT': [feature5],
    'K_SH_POST': [feature6],
    'ant_im': [feature7],
    'ROE': [feature8],
    # Include other features
}

user_data = pd.DataFrame(user_input)

# Make predictions
if st.button('Predict'):
    prediction = model.predict(user_data)
    if prediction == 0:
        st.success('no heart problem')
    elif prediction == 1:
        st.error('cardiogenic shock')
    elif prediction == 2:
        st.error('pulmonary enema')
    elif prediction == 3:
        st.error('myocardinal rupture')
    elif prediction == 4:
        st.error('progress of congestive heart failure')
    elif prediction == 5:
        st.error('thromboembolism')
    elif prediction == 6:
        st.error('asystole')
    else:
        st.error('ventricular fibrillation')
st.text('Note: Click "Predict" to see the prediction result.')
