from sklearn.linear_model import LogisticRegression
import numpy as np

# Dummy training data (replace later with real data / Spark)
X = np.array([
    [1, 0],
    [0, 1],
    [1, 1],
    [0, 0]
])
y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

def predict(features: list):
    return int(model.predict([features])[0])
