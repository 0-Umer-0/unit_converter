import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🔄 Unit Converter")

# Category Selection
category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

# Length Converter
def convert_length(value, from_unit, to_unit):
    units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254}
    return value * units[from_unit] / units[to_unit]

# Weight Converter
def convert_weight(value, from_unit, to_unit):
    units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495}
    return value * units[from_unit] / units[to_unit]

# Temperature Converter
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Inputs
value = st.number_input("Enter the value to convert", value=0.0, format="%.4f")

if category == "Length":
    from_unit = st.selectbox("From", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    to_unit = st.selectbox("To", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"])
    result = convert_length(value, from_unit, to_unit)

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilogram", "Gram", "Pound", "Ounce"])
    to_unit = st.selectbox("To", ["Kilogram", "Gram", "Pound", "Ounce"])
    result = convert_weight(value, from_unit, to_unit)

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

# Output
st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
