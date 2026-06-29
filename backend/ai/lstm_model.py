import numpy as np

class LSTMModel:

    def __init__(self):
        print("LSTM Model Initialized")

    def predict(self, data):

        prediction = np.random.choice(
            ["BUY", "SELL", "HOLD"],
            p=[0.4,0.4,0.2]
        )

        confidence = np.random.randint(70,95)

        return prediction, confidence
