import streamlit as st
import pickle
import numpy as np

xgbc = pickle.load(open(r'C:\Users\vbts0\Downloads\xgbc.pkl', 'rb'))
def main():
    st.title("PCOS Prediction App")
    st.subheader("Enter the input values")
    

    input_values = [
        st.number_input("Age in years", value=5),
        st.number_input("Weight in kg", value=20),
        st.number_input("Height(Cm)", value=0),
        st.number_input("BMI(Body Mass Index)", value=55.6),
        st.number_input("Pulse rate(bpm)", value=180.0),
        st.number_input("RR (breaths/min)", value=11),
        st.number_input("Hemoglobin(g/dl)", value=66),
        st.number_input("Cycle(Regular/Irregular). Enter 2 for regular and 4 for irregular", value=2),
        st.number_input("Cycle length(days)", value=10.48),
        st.number_input("Pregnant(Y/N)", value=2),
        st.number_input("No. of aborptions", value=5),
        st.number_input("Hip(inch)", value=7.0),
        st.number_input("Waist(inch)", value=0),
        st.number_input("Weight gain(Y/N)", value=0),
        st.number_input("hair growth(Y/N)", value=1.99),
        st.number_input("Skin darkening (Y/N)", value=1.99),
        st.number_input("Hair loss(Y/N)", value=7.95),
        st.number_input("Pimples(Y/N)", value=3.68),
        st.number_input("Fast Food Regular", value=36),
        st.number_input("Regular Exercise", value=30),
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

    threshold_has_pcos = 0.8
    threshold_has_mod_pcos = 0.6
    threshold_has_little_pcos = 0.4

    if probability_has_pcos >= threshold_has_pcos:
        return "PCOS"
    elif probability_has_pcos >= threshold_has_mod_pcos:
        return "Moderate PCOS"
    elif probability_has_pcos >= threshold_has_little_pcos:
        return "Little PCOS"
    else:
        return "No PCOS"
if __name__ == "__main__":
    main()
