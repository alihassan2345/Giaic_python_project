import streamlit as st

st.set_page_config(page_title="unit converter")
st.title("🌍Unit Converter App")
st.write("### 🔄:rainbow[Converts Length, Weight, Time, Tempreature Instantly]")
st.write(" Welcome! Select a category, enter a value and get the converted result in real-time")

category = st.selectbox("Choose a categoty", ["Length", "Weight", "Time" , "Temperature" ])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        elif unit == "Meters to Feet":
            return value * 3.28084
        elif unit == "Feet to Meters":
            return value / 3.28084
        elif unit == "Centimeters to Inches":
            return value / 2.54
        elif unit == "Inches to Centimeters":
            return value * 2.54

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif unit == "Grams to Ounces":
            return value / 28.3495
        elif unit == "Ounces to Grams":
            return value * 28.3495

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Weeks to Days":
            return value * 7
        elif unit == "Days to Weeks":
            return value / 7

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        elif unit == "Kelvin to Celsius":
            return value - 273.15



    return "Invalid unit"
        
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", [
        "Miles to Kilometers", "Kilometers to Miles",
        "Meters to Feet", "Feet to Meters",
        "Centimeters to Inches", "Inches to Centimeters"
    ])
    
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", [
        "Kilograms to Pounds", "Pounds to Kilograms",
        "Grams to Ounces", "Ounces to Grams"
    ])
    
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours",
        "Weeks to Days", "Days to Weeks"
    ])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius",
        "Celsius to Kelvin", "Kelvin to Celsius"
    ])



value = st.number_input("Enter the value to convert")


if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result : .2f}")
    