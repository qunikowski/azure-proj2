import requests as req
import kv_secrets

TRESHOLD = 0.3
URL = kv_secrets.PREDICTOR_URL
PREDICTION_KEY = kv_secrets.PREDICTION_KEY
HEADERS = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/octet-stream"
}


def get_prediction(img):
    response = req.post(URL, data=img, headers=HEADERS)
    predictions = response.json().get("predictions")
    if not predictions or predictions[0].get("probability") < TRESHOLD:
        return None
    return predictions[0]
