import streamlit as st
import pandas as pd

# Load Excel files
@st.cache_data
def load_data():
    ndwi_data = pd.read_excel("ndwi.xlsx")
    ndvi_data = pd.read_excel("ndvi.xlsx")
    castor_seed_data = pd.read_excel("Castor seed.xlsx")
    bajra_data = pd.read_excel("bajra.xlsx")
    return ndwi_data, ndvi_data, castor_seed_data, bajra_data

ndwi_data, ndvi_data, castor_seed_data, bajra_data = load_data()

# Streamlit App
st.title("Data Explorer App")

# Sidebar for dataset selection
dataset_choice = st.sidebar.selectbox("Choose Dataset", ("NDWI", "NDVI", "Castor Seed", "Bajra"))

# Display the selected dataset and filters
if dataset_choice == "NDWI":
    st.subheader("NDWI Data")
    st.write("Filter and view NDWI data")
    
    # Assuming 'Date' and 'Location' columns exist in NDWI data
    date_range = st.date_input("Select Date Range", [])
    location = st.text_input("Enter Location")
    
    # Apply filters
    filtered_data = ndwi_data
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (filtered_data['Date'] <= end_date)]
    if location:
        filtered_data = filtered_data[filtered_data['Location'].str.contains(location, case=False, na=False)]
    
    st.write(filtered_data)

elif dataset_choice == "NDVI":
    st.subheader("NDVI Data")
    st.write("Filter and view NDVI data")
    
    # Assuming 'Date' and 'Location' columns exist in NDVI data
    date_range = st.date_input("Select Date Range", [])
    location = st.text_input("Enter Location")
    
    # Apply filters
    filtered_data = ndvi_data
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_data = filtered_data[(filtered_data['Date'] >= start_date) & (filtered_data['Date'] <= end_date)]
    if location:
        filtered_data = filtered_data[filtered_data['Location'].str.contains(location, case=False, na=False)]
    
    st.write(filtered_data)

elif dataset_choice == "Bajra":
    st.subheader("Bajra Data")
    st.write("Filter and view Bajra data")
    
    # Assuming 'Year', 'State', and 'District' columns exist in Bajra data
    year = st.selectbox("Select Year", options=bajra_data['Year'].unique())
    state = st.selectbox("Select State", options=bajra_data['State'].unique())
    district = st.text_input("Enter District")
    
    # Apply filters
    filtered_data = bajra_data[bajra_data['Year'] == year]
    if state:
        filtered_data = filtered_data[filtered_data['State'] == state]
    if district:
        filtered_data = filtered_data[filtered_data['District'].str.contains(district, case=False, na=False)]
    
    st.write(filtered_data)

else:
    st.subheader("Castor Seed Data")
    st.write("Filter and view Castor Seed data")
    
    # Assuming 'Year', 'State', and 'District' columns exist in Castor Seed data
    year = st.selectbox("Select Year", options=castor_seed_data['Year'].unique())
    state = st.selectbox("Select State", options=castor_seed_data['State'].unique())
    district = st.text_input("Enter District")
    
    # Apply filters
    filtered_data = castor_seed_data[castor_seed_data['Year'] == year]
    if state:
        filtered_data = filtered_data[filtered_data['State'] == state]
    if district:
        filtered_data = filtered_data[filtered_data['District'].str.contains(district, case=False, na=False)]
    
    st.write(filtered_data)
