import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import re

# Data dummy sederhana
data = {
    "password": ["12345", "password", "Pass123", "P@ssw0rd!", "admin", "hello123"],
    "strength": [0, 0, 1, 2, 0, 1]  # 0: Lemah, 1: Sedang, 2: Kuat
}
df = pd.DataFrame(data)

def extract_features(pw):
    return [
        len(pw),
        len(re.findall(r'[A-Z]', pw)),
        len(re.findall(r'[a-z]', pw)),
        len(re.findall(r'[0-9]', pw)),
        len(re.findall(r'[^A-Za-z0-9]', pw)),
    ]

X = df['password'].apply(extract_features).tolist()
y = df['strength']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("Model berhasil disimpan sebagai model.pkl")
