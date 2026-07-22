import pickle
import os


class LaptopPricePredictor:

    def __init__(self, model_path="pipeline.pkl"):

        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model file not found: {self.model_path}"
            )

        with open(self.model_path, "rb") as file:
            model = pickle.load(file)

        return model

    def predict(self, input_df):

        prediction = self.model.predict(input_df)

        return float(prediction[0])

    def predict_multiple(self, input_df):

        prediction = self.model.predict(input_df)

        return prediction