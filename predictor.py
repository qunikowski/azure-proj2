import requests as req

TRESHOLD = 0.3
URL = "https://custom2-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/c3ae4f26-6142-40a5-9f32-aa88f7b3edcf/classify/iterations/model_apple-corn-tomato/image"
HEADERS = {
    "Prediction-Key": "ca45f5702e424b16b87dc74ec7a41300",
    "Content-Type": "application/octet-stream"
}

def get_prediction(img):
    response = req.post(URL, data=img, headers=HEADERS)
    predictions = response.json().get("predictions")
    if not predictions or predictions[0].get("probability") < TRESHOLD:
        return None
    return predictions[0]