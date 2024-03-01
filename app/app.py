from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from joblib import load
import uuid

app = Flask(__name__, static_folder='static')


def floats_strings_to_np_array(floats_string):
    floats = np.array([float(x) for x in floats_string.split(',') if is_float(x)])
    return floats.reshape(len(floats), 1)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@app.route("/", methods=["GET", "POST"])
def hello_world():
    request_type_string = request.method
    filename = "static/base.svg"
    if request_type_string == "GET":
        return render_template('index.html', href=filename)
    else:
        text = request.form['text']
        random_string = uuid.uuid4().hex
        path = "static/" + random_string + ".svg"
        model = load('model.joblib')
        array_to_process = floats_strings_to_np_array(text)
        make_picture("static/AgesAndHeights.pkl", model, array_to_process, path)
        return render_template('index.html', href=path)


def make_picture(training_data_filename, model, new_input_numpy_array, output_file):
    data = pd.read_pickle(training_data_filename)
    ages = data['Age']
    data = data[ages > 0]
    ages = data['Age']
    heights = data['Height']
    x_new = np.array(list(range(19))).reshape(19, 1)
    predictions = model.predict(x_new)
    fig = px.scatter(x=ages, y=heights, title="Height vs Age of People", labels={'x': 'Age (years)',
                                                                                 'y': 'Height (inches)'})
    fig.add_trace(go.Scatter(x=x_new.reshape(19), y=predictions, mode='lines', name='Model'))
    new_predictions = model.predict(new_input_numpy_array)
    fig.add_trace(
        go.Scatter(x=new_input_numpy_array.reshape(len(new_input_numpy_array)), y=new_predictions, name='New Outputs',
                   mode='markers', marker=dict(color='purple', size=20, line=dict(color='purple', width=2))))
    fig.write_image(output_file, width=800, engine='kaleido')
    fig.show()
