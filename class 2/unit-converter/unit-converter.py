import streamlit as st

def convert_unit(value, from_unit, unit_to):

    conversions={ 
        "meter_kilometer": 0.001, #1 meter = 0.001 kilometer
        "kilometer_meter": 1000, #1 kilometer = 1000 meter
        "gram_kilogram": 0.001, #1 gram = 0.001 kilogram
        "kilogram_gram": 1000, #1 kilogram = 1000 gram
    }

    key = f"{from_unit}_{unit_to}"
    if key in conversions:
        conversions = conversions[key]
        return value * conversions  # Fixed incorrect key usage
    else:
        return "Invalid unit"
    
st.title("Unit Converter")
 
value = st.number_input("Enter the value to convert:")

unit_from = st.selectbox("Select the unit to convert from:",["meter","kilometer","gram","kilogram"] )

unit_to = st.selectbox("convert to:",["meter","kilometer","gram","kilogram"] )

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")  # Fixed indentation
else "invalid input"