import streamlit as st
import pandas as pd

# Load Excel files
@st.cache_data
def load_data():
    ndwi_data = pd.read_excel("https://docs.google.com/spreadsheets/d/1y6pBlXs8SIvWZD3bhNSKYz8ZNLvhZSa6/export?format=xlsx")
    ndvi_data = pd.read_excel("https://docs.google.com/spreadsheets/d/1DwEz51UY7GJ2GL18OfYBQQXRV9daVeBT/export?format=xlsx")
    castor_seed_data = pd.read_excel("https://docs.google.com/spreadsheets/d/1D_IQkrc53XWe0k9XCs9LsHqGnDFFO94h/export?format=xlsx")
    bajra_data = pd.read_excel("https://docs.google.com/spreadsheets/d/1w57VzMQVvQVGFpwIkp5tQFdrV4ruUIC_/export?format=xlsx")
    

    # Convert 'DateTime' columns if they exist
    for dataset, name in zip([ndwi_data, ndvi_data], ['NDWI', 'NDVI']):
        if 'DateTime' in dataset.columns:
            dataset['DateTime'] = pd.to_datetime(dataset['DateTime'], errors='coerce')
            dataset.dropna(subset=['DateTime'], inplace=True)
        else:
            st.warning(f"DateTime column not found in {name} dataset.")

    return ndwi_data, ndvi_data, castor_seed_data, bajra_data

ndwi_data, ndvi_data, castor_seed_data, bajra_data = load_data()

# Streamlit App
st.title("Data Explorer App")

# Sidebar for dataset selection
dataset_choice = st.sidebar.selectbox("Choose Dataset", ("NDWI", "NDVI", "Castor Seed", "Bajra"))

# Function to filter data based on date range and location
def filter_data(data, date_range, location):
    filtered_data = data
    if 'DateTime' in data.columns and len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered_data = filtered_data[(filtered_data['DateTime'] >= start_date) & (filtered_data['DateTime'] <= end_date)]
    if 'Location' in data.columns and location:
        filtered_data = filtered_data[filtered_data['Location'].str.contains(location, case=False, na=False)]
    return filtered_data

# NDWI Dataset Section
if dataset_choice == "NDWI":
    st.subheader("NDWI Data")
    st.write("Filter and view NDWI data")

    date_range = st.date_input("Select Date Range", [])
    location = st.text_input("Enter Location")

    filtered_data = filter_data(ndwi_data, date_range, location)
    st.write(filtered_data)

# NDVI Dataset Section
elif dataset_choice == "NDVI":
    st.subheader("NDVI Data")
    st.write("Filter and view NDVI data")

    date_range = st.date_input("Select Date Range", [])
    location = st.text_input("Enter Location")

    filtered_data = filter_data(ndvi_data, date_range, location)
    st.write(filtered_data)

# Bajra Dataset Section
elif dataset_choice == "Bajra":
    st.subheader("Bajra Data")
    st.write("Filter and view Bajra data")
    
    year = st.selectbox("Select Year", options=bajra_data['Year'].unique())
    state = st.selectbox("Select State", options=bajra_data['State'].unique())
    district = st.text_input("Enter District")
    
    filtered_data = bajra_data[bajra_data['Year'] == year]
    if state:
        filtered_data = filtered_data[filtered_data['State'] == state]
    if district:
        filtered_data = filtered_data[filtered_data['District'].str.contains(district, case=False, na=False)]
    
    st.write(filtered_data)

# Castor Seed Dataset Section
else:
    st.subheader("Castor Seed Data")
    st.write("Filter and view Castor Seed data")
    
    year = st.selectbox("Select Year", options=castor_seed_data['Year'].unique())
    state = st.selectbox("Select State", options=castor_seed_data['State'].unique())
    district = st.text_input("Enter District")
    
    filtered_data = castor_seed_data[castor_seed_data['Year'] == year]
    if state:
        filtered_data = filtered_data[filtered_data['State'] == state]
    if district:
        filtered_data = filtered_data[filtered_data['District'].str.contains(district, case=False, na=False)]
    
    st.write(filtered_data)
