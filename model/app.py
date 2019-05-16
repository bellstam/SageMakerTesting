import flask
from flask import Flask, Response
import pandas as pd
from io import StringIO
from model import ProphetModel
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    """
    Determine if the container is healthy by running a sample through the algorithm.
    """
    # we will return status ok if the model doesn't barf
    # but you can also insert slightly more sophisticated tests here
    return Response(response='{"status": "ok"}', status=200, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def predict():
    """
    Do an inference on a single batch of data.
    """

    model_parameters = {'changepoint_prior_scale': 1,
                    'seasonality_mode': 'multiplicative',
                    'target_column': 'y_log',
                    'seasonality': {
                        'daily': {
                            'period': 1,
                            'fourier_order': 4,
                            'prior_scale': 10
                        },
                        'weekly': {
                            'period': 7,
                            'fourier_order': 3,
                            'prior_scale': 10
                        },
                        'monthly': {
                            'period': 30.5,
                            'fourier_order': 4,
                            'prior_scale': 10
                        }
                    }}

    m = ProphetModel(model_parameters)

    # format into a csv
    results_str = ",\n".join("sdlkfmaslkmfklsadf")#(results.astype('str'))

    # return
    return Response(response=results_str, status=200, mimetype='text/csv')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
