import streamlit as st
import pickle
import pandas as pd
import folium
from streamlit_folium import folium_static
import mysql.connector

# Load the trained model
model = pickle.load(open('models/GridSearchRandomForest_4var-copy1.pkl', 'rb'))
#model_3var_1 = pickle.load(open('models/_combinations1_model.pkl', 'rb'))
#model_3var_2 = pickle.load(open('models/_combinations2_model.pkl', 'rb'))


# Function to predict pH values
def predict_ph(variables):
    # Prepare the input data
    data = pd.DataFrame(variables, index=[0])

    # Make pH prediction
    ph_value = model.predict(data)[0]

    return ph_value


# Save data to MySQL
def save_to_mysql(variables, latitude, longitude, ph_value):
    # Connect to MySQL
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost', database='projet1')

    # Create a cursor
    cursor = cnx.cursor()

    # Define the SQL query to insert data
    query = "INSERT INTO api_datapoint (variable1, variable2, variable3, variable4, latitude, longitude, ph_value) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    # Execute the query with the values
    cursor.execute(query, (variables['CTDTMP [ITS-90]'], variables['PHSPHT [UMOL/KG]'],
                           variables['SILCAT [UMOL/KG]'], variables['TCARBN [UMOL/KG]'],
                           latitude, longitude, ph_value))

    # Commit the changes
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()


# Streamlit app
def main():
    st.title('Traitement des données océanographique')

    # User input form
    st.subheader('Enter the variables:')

    ctdtmp = st.number_input('CTDTMP [ITS-90]')
    phspht = st.number_input('PHSPHT [UMOL/KG]')
    silcat = st.number_input('SILCAT [UMOL/KG]')
    tcarbn = st.number_input('TCARBN [UMOL/KG]')
    latitude = st.number_input('Latitude')
    longitude = st.number_input('Longitude')

    # Create a dictionary of user input variables
    variables = {
        'CTDTMP [ITS-90]': ctdtmp,
        'PHSPHT [UMOL/KG]': phspht,
        'SILCAT [UMOL/KG]': silcat,
        'TCARBN [UMOL/KG]': tcarbn,
    }

    # Predict pH value
    ph_value = predict_ph(variables)


    # Display the predicted pH value
    st.subheader('Predicted pH Value:')
    st.markdown(f'<p style="font-size:24px">{ph_value}</p>', unsafe_allow_html=True)

    # Save data to MySQL
    if st.button('Save'):
        if all(variables.values()):
            # Save data to MySQL
            save_to_mysql(variables, latitude, longitude, ph_value)
            st.success('Data saved successfully!')
        else:
            st.warning('Please enter all four variables before saving to the database.')

    # Create a map with the user's input location
    st.subheader('Map')
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup=f'Latitude: {latitude}, Longitude: {longitude}, pH: {ph_value}').add_to(m)
    folium_static(m)


if __name__ == '__main__':
    main()
