# Project: Diamond Price Prediction API

## Overview and Objectives
This project aims to predict the price of diamonds based on their characteristics (carat, cut, color, etc.). The final product is a Flask API that serves predictions from a trained machine learning model.

## How to Run This Project

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/trivedidhriti2003/bootcamp_Dhriti_Trivedi.git](https://github.com/trivedidhriti2003/bootcamp_Dhriti_Trivedi.git)
    cd bootcamp_Dhriti_Trivedi/Stage\ 13\:\ Productization/
    ```
2.  **Set Up Virtual Environment and Install Dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Run the Flask API**
    ```bash
    python app.py
    ```
    The API will be available at `http://127.0.0.1:5000`.

4.  **Test the API**
    You can see example API calls in the `notebooks/01_model_training_and_api_test.ipynb` notebook.

## API Endpoints

* `POST /predict`: Sends a JSON object with diamond features and returns a price prediction.
* `GET /plot`: Generates and saves a new feature analysis plot in the `/static` directory.

## Assumptions and Risks
* **Assumption**: The training data is representative of the diamonds for which predictions will be made.
* **Risk**: The model's performance may degrade over time if the diamond market changes. It may need periodic retraining.
