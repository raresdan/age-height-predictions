from flask import Flask
import numpy as np
from joblib import load

app = Flask(__name__)


@app.route("/")
def hello_world():
    test_np_input = np.array([[1], [2], [17]])
    model = load('model.joblib')
    predictions = model.predict(test_np_input)
    predictions_as_string = str(predictions)
    return predictions_as_string

# 26:16
