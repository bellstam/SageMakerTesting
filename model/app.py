from datetime import timedelta
from flask import Flask, request, jsonify, Response
import pandas as pd
import io
from models.prophet_model import ProphetModel
app = Flask(__name__)


forward_steps = 192
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
    if request.method == 'POST':
        if request.content_type == 'text/csv':
            df = pd.read_csv(io.BytesIO(request.data), encoding='utf8')
            m = ProphetModel(model_parameters)
            m.model_object.fit(df)
            last_valid_hour_utc = pd.to_datetime(df.tail(1)['ds'].values[0])
            future = pd.DataFrame({'ds': pd.date_range(start=last_valid_hour_utc + timedelta(hours=1),
                                                   end=last_valid_hour_utc + timedelta(hours=forward_steps),
                                                   freq='H')})
            # run prediction
            results_str = m.model_object.predict(future).to_csv(index=False)

        else:
            return Response(response='This predictor only supports CSV data', status=415, mimetype='text/plain')



    # return
    return Response(response=results_str, status=200, mimetype='text/csv')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
