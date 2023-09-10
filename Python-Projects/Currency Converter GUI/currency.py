import streamlit as st

st.title("Currency converter")

currency = st.radio("Select Currency: ", ('Rupee', 'Dollar',"Euro"))

currency_into_convert = st.radio("Select Currency into convert: ", ('Rupee', 'Dollar',"Euro"))

amount=st.number_input("Enter amount:")

if currency.lower()=="rupee":
    
    if currency_into_convert.lower() == "dollar":        
        rupee_value=0.01204 #st.number_input("Enter value of 1 rupee in dollar")        
        st.success(f"₹ {amount} is :   $ {rupee_value*amount} ")
        
    elif currency_into_convert.lower() == "rupee":
        st.success(f"₹ {amount} is :  ₹ {amount}")
        
    elif currency_into_convert.lower() == "euro":
        rupee_value=0.01125 #st.number_input("Enter value of 1 rupee in euro")
        st.success(f"₹ {amount} is :   € {rupee_value*amount}")
        
elif currency.lower()=="dollar":
    
    if currency_into_convert.lower() == "dollar":
        st.success(f"$ {amount} is:  $ {amount} ")
        
    elif currency_into_convert.lower() == "rupee":
        dollar_value=83.045  #st.number_input("Enter value of 1 dollar in rupee")
        st.success(f"$ {amount} is: ₹ {dollar_value*amount}")
        
    elif currency_into_convert.lower() == "euro":
        dollar_value=0.93395  #st.number_input("Enter value of 1 dollar in euro")
        st.success(f"$ {amount} is: € {dollar_value*amount}")
else:
    
    if currency_into_convert.lower() == "dollar":
        euro_value=1.07072 #st.number_input("Enter value of 1 euro in dollar")
        st.success(f"€ {amount} is: $ {euro_value*amount} ")
        
    elif currency_into_convert.lower() == "rupee":
        euro_value= 88.91803 #st.number_input("Enter value of 1 euro in rupee")
        st.success(f" € {amount} is: ₹ {euro_value*amount}")
        
    elif currency_into_convert.lower() == "euro":
        st.success(f" € {amount} is: € {amount}")   