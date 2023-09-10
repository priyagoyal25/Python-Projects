import streamlit as st

st.set_page_config("BMI calculator")
st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=0.1, step=0.1)
unit=st.radio("Choose height :",("meter","centi meter","inches","foot"))
height = st.number_input("Enter your height :", min_value=0.1, step=0.01)

if st.button("Calculate BMI"):
    if unit == "meter":
        bmi = weight / (height ** 2)
    elif unit == "centi meter":
        height=height/100
        bmi = weight / (height ** 2)
    elif unit == "inches":
        height=height*0.0254
        bmi = weight / (height ** 2) 
    else:
        height=height*0.3048
        bmi = weight / (height ** 2) 

    st.subheader(f":green[Your BMI: {bmi:.2f}]")

    if bmi < 18.5:
        st.warning(f":red[You are underweight.]")
    elif 18.5 <= bmi < 24.9:
        st.success(f":red[You are in a healthy weight range.]")
    elif 25 <= bmi < 29.9:
        st.warning(f":red[You are overweight.]")
    else:
        st.warning(f":red[You are obese.]")




