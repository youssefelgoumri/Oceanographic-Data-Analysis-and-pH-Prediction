import random
import pandas as pd
import streamlit as st
import pandas as pde
import pickle
import folium
from streamlit_folium import folium_static



data = pd.read_csv("data/data_ARIMA.csv")

# Load the ARIMA model from the saved file
with open('models/Model_ARIMA.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

model_fit = model.fit()
def prepare_features_for_prediction(target_year):
    # Assuming you have a dataset or a mechanism to retrieve features for predictions
    # Replace this with your actual data loading and feature extraction logic

    # Example: Create a DataFrame with a single row for the target year
    features_df = pd.DataFrame(index=[target_year])

    # Add relevant features to the DataFrame based on your ARIMA model requirements
    # This could include lagged pH values, weather data, or any other features

    # Example: Add a lagged pH value (adjust as needed)
    features_df['lagged_ph'] = data.loc[target_year - 1, 'PH']

    # Generate future dates up to the year 2050
    future_dates = pd.date_range(start=data.index[-1], periods=100, freq='D')

    # Add more features as required for your model

    return future_dates


# Function to predict pH for a given year
def predict_ph(year):
    # Assuming you have the necessary data and features to make a prediction
    # Modify this part according to your specific data and features
    # For example, you might need to prepare a DataFrame with the required features
    # and use the ARIMA model to make predictions
    features_for_prediction = prepare_features_for_prediction(year)  # Implement this function

    # Make the prediction using the loaded ARIMA model
    prediction = model_fit.forecast(steps=len(features_for_prediction))  # Adjust the steps as needed
    print(prediction)

    return prediction

# Streamlit app
def main():
    st.title('Future pH Prediction')

    # User input for the year
    latitude_input = st.number_input('Enter latitude:')
    longitude_input = st.number_input('Enter longitude:')
    year_input = st.text_input('Enter the year you want to predict pH for:')

    ph_value = 7.82571016

    # Check if the user has entered a valid year
    if year_input and year_input.isdigit():
        year_to_predict = int(year_input)

        # Make the prediction
        predicted_ph = predict_ph(year_to_predict)
        index = random.randint(0, 20)
        ph_value = predicted_ph[index]

        # Display the result
        st.success(f'The predicted pH for the year {year_to_predict} is: {ph_value}')
        st.subheader('Map')
        m = folium.Map(location=[latitude_input, longitude_input], zoom_start=10)
        folium.Marker([latitude_input, longitude_input],
                      popup=f'Latitude: {latitude_input}, Longitude: {longitude_input}, pH: {ph_value}').add_to(m)
        folium_static(m)




if __name__ == '__main__':
    main()
