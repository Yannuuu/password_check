from flask import Flask, request, jsonify, render_template
import joblib
from utils.features import extract_features

app = Flask(__name__)

# Load model dari folder 'model'
model = joblib.load("model/manual_password_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    password = request.form.get('password') or request.json.get('password')
    if not password:
        return jsonify({'error': 'Password required'}), 400
    
    features = extract_features(password)
    strength = model.predict(features)[0]
    
    # Jika form HTML kirim, tampilkan di browser
    if request.form:
        return render_template("index.html", result=strength, password=password)
    
    return jsonify({'strength': strength})

if __name__ == '__main__':
    app.run(debug=True)
