# 📈Age vs Height predicitor

This project is a simple web application built using Flask, incorporating a Linear Model developed with Scikit-learn to estimate the height of teenagers based on their age. The application provides an interactive plotting feature using Plotly, allowing users to input a specific age and visualize the corresponding height estimation made by the model.

## Features

- **Flask Web Application:** Utilizes Flask to create a user-friendly web interface.
- **Linear Model:** Implements a Linear Model using Scikit-learn, trained on a dataset in pickel format, containing age and height data of teenagers. Saved & Loaded the model using Joblib.
- **Interactive Plotting:** Incorporates Plotly to generate interactive plots, enabling users to input age parameters and visualize height estimations in real-time.
- **User-friendly Interface:** Offers a seamless user experience with intuitive controls for age input and dynamic visualization of height estimations.

## Usage

1. Clone the repository:

    ```
    git clone https://github.com/raresdan/age-height-predictions
    ```

2. Navigate to the project directory:

    ```
    cd age-height-predictions
    ```

3. Set up and activate a virtual environment:

    ```
    py -m venv .env
    .env/Scripts/activate   # For Windows
    ```

4. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Run the Flask application:

    ```
    cd app
    flask run
    ```

6. Access the application through your web browser at your local host.
