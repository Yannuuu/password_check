import pandas as pd

def extract_features(password):
    return pd.DataFrame([{
        "length": len(password),
        "digits": sum(c.isdigit() for c in password),
        "uppers": sum(c.isupper() for c in password),
        "lowers": sum(c.islower() for c in password),
        "symbols": sum(not c.isalnum() for c in password)
    }])