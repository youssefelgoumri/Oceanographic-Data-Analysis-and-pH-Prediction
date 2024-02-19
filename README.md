# Oceanographic Data Analysis and pH Prediction
This repository contains the code for the Oceanographic Data Analysis and pH Prediction project. The project aims to develop an application that predicts pH values in the ocean based on user input of oceanographic variables.

## Features
* Input oceanographic variables and predict pH values
* Import CSV files with oceanographic data and visualize on a map
* Store user data and prediction results in a MySQL database
* Forecasting pH values over years
* Interactive map visualization using Folium library

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/youssefelgoumri/Oceanographic-Data-Analysis-and-pH-Prediction.git
   
2. Install the required dependencies:
   ```
   pip install -r requirements.txt

3. Download the folders models and data

   ```/models``` : https://drive.google.com/drive/folders/1j1iaL2LFsw8Gpi5vxzEh5_torrhT2yVK?usp=sharing

   ``` /data ``` : https://drive.google.com/drive/folders/1s82lpfKPN3FEi4mJaNwXxkUlnfKAmlPI?usp=sharing


## Usage
1. Run the Streamlit application:
   ```
   streamlit run app.py

2. Access the application in your web browser at http://localhost:8501.

##  Interface :

* Enter data
![app-features](https://github.com/youssefelgoumri/Oceanographic-Data-Analysis-and-pH-Prediction/assets/94170257/acbd2b7f-6845-4670-8da3-85dcfd5e708f)

* Predict the pH value and display the map
![app-ph-map](https://github.com/youssefelgoumri/Oceanographic-Data-Analysis-and-pH-Prediction/assets/94170257/8feebd70-4cb7-4dde-8002-a59d523dd363)

* Importing excel data and display it in the map
![csv-map](https://github.com/youssefelgoumri/Oceanographic-Data-Analysis-and-pH-Prediction/assets/94170257/14c165e8-b2b2-4501-af1a-81194b5cccc0)

* Forcasting pH value over years
![Screenshot 2024-01-31 161827](https://github.com/youssefelgoumri/Oceanographic-Data-Analysis-and-pH-Prediction/assets/94170257/3210b378-92f1-4519-9059-5aa7806e2b82)


## License
This project is licensed under the [MIT License](LICENSE).
