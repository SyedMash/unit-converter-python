import streamlit as st


def remove_selected(array:list, string:str):
    array.remove(string)
    return array

def length_converter(value, from_unit, to_unit):
    length_unit = {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Nautical Miles": 1852,
        "Inches": 0.3048,
        "Feet": 0.3048,
        "Yards": 0.9144,
    }
    return value * (length_unit[from_unit] / length_unit[to_unit])

def weight_converter(value, from_unit, to_unit):
    weight_unit = {
        "Grams": 1000,
        "Kilograms": 0.001,
        "Hectograms": 0.01,
        "Milligrams": 1000,
        "Ounces": 0.035274,
    }
    return value * (weight_unit[to_unit] / weight_unit[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
st.title("Unit Converter App")

selected_type = st.selectbox("Select a type", ["Length", "Weight", "Temperature"])

if selected_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Nautical Miles", "Inches", "Feet", "Yards"]
    from_unit = st.selectbox("From", units)
    new_unit = remove_selected(units, from_unit)
    to_unit = st.selectbox("To", new_unit)
    value = st.number_input("Value")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result} {to_unit}")

elif selected_type == "Weight":
    units = ["Kilograms", "Hectograms", "Grams", "Milligrams", "Ounces"]
    from_unit = st.selectbox("From", units)
    new_unit = remove_selected(units, from_unit)
    to_unit = st.selectbox("To", new_unit)
    value = st.number_input("Value")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result} {to_unit}")

elif selected_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    new_unit = remove_selected(units, from_unit)
    to_unit = st.selectbox("To", new_unit)
    value = st.number_input("Value")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value}{from_unit} is equal to {result} {to_unit}")
