import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static


# Function to read landmarks data from uploaded file
def read_landmarks_data(file):
    if file:
        landmarks_data = pd.read_csv(file)
        return landmarks_data
    return None


# Streamlit app
def main():
    st.title('Traitement des données océanographique')

    # File uploader for landmarks data
    uploaded_file = st.file_uploader('Upload csv file', type=['csv'])

    # Read landmarks data from uploaded file
    landmarks_data = read_landmarks_data(uploaded_file)

    # Check if landmarks data is available
    if landmarks_data is not None:
        # Create a map
        m = folium.Map()

        # Add markers for each landmark
        for index, row in landmarks_data.iterrows():
            latitude = row['Latitude [degrees_north]']
            longitude = row['Longitude [degrees_east]']
            ph = row['PH']
            popup_text = f'Latitude: {latitude}\nLongitude: {longitude}\npH: {ph}'
            folium.Marker([latitude, longitude], popup=popup_text).add_to(m)

        # Display the map
        folium_static(m)
    else:
        st.write('Please upload an csv file.')


if __name__ == '__main__':
    main()
