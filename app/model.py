import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "app/model.joblib"

def train_model():
    X = np.array([
        [45, 120, 200],
        [50, 130, 250],
        [30, 110, 180],
        [60, 140, 260]
    ])
    y = np.array([0, 1, 0, 1])

    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    return model

def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except:
        return train_model()
