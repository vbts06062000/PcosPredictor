import streamlit as st
import pickle
import numpy as np
import datetime

xgbc = pickle.load(open(r'C:\Users\vbts0\Downloads\xgbc.pkl', 'rb'))

st.set_page_config(
    page_title="PCOS PREDICTION",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded", 
    background_color="#bca6d6", 
)


# Set page configuration
st.set_page_config(
    page_title="PCOS PREDICTION",  # Page title
    page_icon=":smiley:",  # Page icon
    layout="wide",  # Layout of the page
    initial_sidebar_state="expanded",  # Initial state of the sidebar
    background_color="#bca6d6",  # Background color of the page
)

# Add content to the page
st.title("Welcome to the PCOS Prediction App!")
st.write("Here you can predict the likelihood of having PCOS based on various factors.")

# Add input forms, data processing, and prediction code here
# Your Streamlit app content goes here

def main():
    st.title("PCOS Prediction App")
    
    name = st.text_input("Enter your name:")
    #st.write.subheader('Welcome', name)
    if name:
        st.subheader(f"Welcome, {name}!")
    
    min_date = datetime.date(1950, 1, 1)
    max_date = datetime.date(2024, 12, 31)

    d = st.date_input("When's your birthday", datetime.date(1990, 7, 6), min_value=min_date, max_value=max_date)
    st.write('Your birthday is:', d)

    st.subheader("Please enter the following details")
    input_values = [
        st.number_input("What is your Age in years", value=20),
        st.number_input("What is your Weight in kg", value=50),
        st.number_input("What is your Height(Cm)", value=150),
        st.number_input("What is your BMI(Body Mass Index)", value=25),
        st.number_input("What is your Pulse rate (bpm)", value=80.0),
        st.number_input("What is your RR (breaths/min)", value=15),
        st.number_input("What is yourHemoglobin (g/dl)", value=14),
        st.number_input("Are you Cycles Regular or Irregular. Enter 2 for regular and 4 for irregular", value=2),
        st.number_input("What is your Cycle length(days)", value=4),
        st.number_input("Are you Pregnant (Y/N)", value=0),
        st.number_input("No. of aborptions (if any)", value=0),
        st.number_input("What is your Hip(inch)", value=30),
        st.number_input("What is your Waist(inch)", value=30),
        st.number_input("Have you experienced Weight gain(Y/N)", value=0),
        st.number_input("Have you experienced hair growth(Y/N)", value=0),
        st.number_input("Have you experienced Skin darkening (Y/N)", value=1),
        st.number_input("Have you experienced Hair loss(Y/N)", value=1),
        st.number_input("Have you experienced extreme Pimples(Y/N)", value=1),
        st.number_input("Do you reguarly eat Fast Food ?", value=1),
        st.number_input("Do you regularly Exercise ?", value=1),
        ]

    # Convert the input values to a list
    input_values = [val for val in input_values]

    # Predict the result
    result = predict(xgbc, input_values)

    # Display the result
    st.header("Result")
    st.write(result)

def predict(model, input_value):
    input_value = np.array(input_value).reshape(1, -1)
    probabilities = model.predict_proba(input_value)

    probability_has_pcos = probabilities[0, 1]
    #return probability_has_pcos
    st.markdown(f"<p style='font-size:{"20px"}; color:{"white"}'>Probability of having PCOS: {probability_has_pcos*100} % </p>", unsafe_allow_html=True)

    threshold_has_pcos = 0.8
    threshold_has_mod_pcos = 0.6
    threshold_has_little_pcos = 0.4

    if probability_has_pcos >= threshold_has_pcos:
        return "There is a high chance that you may have PCOS. We strongly recommend consulting with a gynecologist, particularly if you've been consistently skipping menstrual cycles, for a thorough evaluation and personalized guidance on managing your health."
    elif probability_has_pcos >= threshold_has_mod_pcos:
        return "There appears to be a moderate likelihood that you may be experiencing Polycystic Ovary Syndrome (PCOS). We recommend seeking consultation with a gynecologist, especially if you are experiencing irregular menstrual cycles. While PCOS may not pose immediate health risks, adopting a balanced diet and incorporating regular exercise into your routine can help manage symptoms and promote overall well-being. "
    elif probability_has_pcos >= threshold_has_little_pcos:
        return "There appears to be a lesser likelihood that you may be experiencing Polycystic Ovary Syndrome (PCOS)"
    else:
        return "No PCOS"
if __name__ == "__main__":
    main()