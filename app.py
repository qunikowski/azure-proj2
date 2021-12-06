from flask import Flask, render_template, request,  jsonify, make_response, redirect, url_for
import db
import predictor as pre
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/stats')
def stats():
    predictions = db.get_last_week_predictions()
    return render_template("stats.html", predictions=predictions)

@app.route('/upload', methods=['POST'])
def upload():
    img = request.files['file'].read()
    prediction = pre.get_prediction(img)
    prediction = db.add_prediction(img, prediction)
    return render_template("index.html", prediction=prediction)
    
@app.route("/show/<int:id>")
def show(id):
    image = db.get_image(id)
    response = make_response(image)
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set('Content-Disposition', 'attachment', filename='%s.jpg' % id)
    return response

if __name__ == '__main__':    
    app.run(debug=True, port=5000)