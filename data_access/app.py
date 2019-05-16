import flask
from flask import Flask, Response
import pandas as pd
import numpy as np


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

    results = pd.DataFrame({'ds': pd.date_range(start='2019-01-01', end='2019-01-31', freq='H'),
                            'y': np.random.lognormal(3, 1, 721)})
    # format into a csv
    results_str = results.to_csv(index=False)

    # return
    return Response(response=results_str, status=200, mimetype='text/csv')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
