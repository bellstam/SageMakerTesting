import flask
from flask import Flask, Response
import pandas as pd
from io import StringIO
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

    #results = run_model(X_train)

    # format into a csv
    results_str = ",\n".join("sdlkfmaslkmfklsadf")#(results.astype('str'))

    # return
    return Response(response=results_str, status=200, mimetype='text/csv')


