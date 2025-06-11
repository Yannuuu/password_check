from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("manual_password_model.pkl")

def extract_features(password):
    return pd.DataFrame([{
        "length": len(password),
        "digits": sum(c.isdigit() for c in password),
        "uppers": sum(c.isupper() for c in password),
        "lowers": sum(c.islower() for c in password),
        "symbols": sum(not c.isalnum() for c in password)
    }])

@app.route('/')
def home():
    return "API aktif!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    password = data.get("password", "")
    if not password:
        return jsonify({"error": "Password is required"}), 400

    features = extract_features(password)
    strength = model.predict(features)[0]
    return jsonify({"strength": strength})
