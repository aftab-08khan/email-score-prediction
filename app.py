from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/email_score_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

@app.route("/predict-score", methods=["POST"])
def predict_score():
    data = request.json
    email_description = data["email_description"]
    
    X = vectorizer.transform([email_description])
    
    score = model.predict(X)[0]
    
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)