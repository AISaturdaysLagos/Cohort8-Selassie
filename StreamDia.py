import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(open("model.joblib", "rb"))

def main():
    st.sidebar.header('Diabetes Risk Prediction')
    st.sidebar.text('This is a web app that determines the risk of diabetes')
    st.sidebar.header('Kindly fill in the appropriate information')

    # Create Streamlit widgets for user inputs
    gender = st.radio("Select Gender", ["Male", "Female", "Others"])
    age = st.slider("Choose your age", 25, 70)
    degree = st.radio("Select Education", ["Educated", "Non-Educated"])
    income_range = st.slider("Select Income Range", 10000, 100000)
    bmi = st.slider("Input your BMI", 0, 20)
    high_bp = st.checkbox("Do you have high blood pressure?")
    high_chol = st.checkbox("Do you have high cholesterol?")
    chol_check = st.slider("Input your Cholesterol", 0, 20)
    smoker = st.checkbox("Do you smoke?")
    stroke = st.checkbox("Do you have a stroke?")
    heart_disease_or_attack = st.checkbox("Do you have any heart diseases?")
    phys_activity = st.checkbox("Do you perform physical activities?")
    
    # Additional features
    fruits = st.checkbox("Do you consume fruits?")
    veggies = st.checkbox("Do you consume veggies?")
    hvy_alcohol_consumption = st.checkbox("Do you have heavy alcohol consumption?")
    any_healthcare = st.checkbox("Do you have any healthcare?")
    no_doc_bc = st.checkbox("Do you have NoDocbc?")
    gen_health = st.checkbox("Do you have general health issues?")
    ment_health = st.checkbox("Do you have mental health issues?")
    phys_health = st.checkbox("Do you have physical health issues?")
    diff_walk = st.checkbox("Do you experience difficulty walking?")

    # Create a dictionary to hold user input
    input_dict = {
        'BMI': bmi,
        'HighBP': high_bp,
        'HighChol': high_chol,
        'CholCheck': chol_check,
        'Smoker': smoker,
        'Stroke': stroke,
        'HeartDiseaseorAttack': heart_disease_or_attack,
        'PhysActivity': phys_activity,
        'Fruits': fruits,
        'Veggies': veggies,
        'HvyAlcoholConsump': hvy_alcohol_consumption,
        'AnyHealthcare': any_healthcare,
        'NoDocbcCost': no_doc_bc,
        'GenHlth': gen_health,
        'MentHlth': ment_health,
        'PhysHlth': phys_health,
        'DiffWalk': diff_walk,
        'Sex': gender,
        'Age': age,
        'Education': degree,
        'Income': income_range,
        
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensuring the columns match the columns used during training
    #input_df = input_df[['BMI', 'HighBP', 'HighChol', 'CholCheck', 'Smoker', 'Stroke',
                         #'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump',
                          #'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth','DiffWalk',
                          #'Sex','Age', 'Education', 'Income']]
    
    #if feature_names != model.feature_names:
        #st.error("Feature names/order mismatch. Please check your input features.")



    if st.button("Predict"):
        prediction = model.predict(input_df)[0]
        st.subheader('Prediction')
        st.write(f'The predicted diabetes risk is: {prediction}')

if __name__ == "__main__":
    main()











