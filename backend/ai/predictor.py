from ai.lstm_model import LSTMModel

class Predictor:

    def __init__(self):
        self.model = LSTMModel()

    def predict(self, dataframe):

        signal, confidence = self.model.predict(dataframe)

        return {
            "signal": signal,
            "confidence": confidence
        }
