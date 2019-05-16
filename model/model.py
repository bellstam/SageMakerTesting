from fbprophet import Prophet

class ProphetModel:

    def __init__(self, model_parameters):
        self.model_parameters = model_parameters
        self.model_object = self.define_model()

    def define_model(self):
        model_object = Prophet(changepoint_prior_scale=self.model_parameters['changepoint_prior_scale'],
                               seasonality_mode=self.model_parameters['seasonality_mode'],
                               yearly_seasonality=False,
                               weekly_seasonality=False,
                               daily_seasonality=False)

        if 'seasonality' in self.model_parameters:
            for season in self.model_parameters['seasonality']:
                model_object.add_seasonality(name=season, **self.model_parameters['seasonality'][season])

        return model_object