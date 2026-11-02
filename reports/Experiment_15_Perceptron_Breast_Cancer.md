# AI LAB – 4

## EXPERIMENT 15 - Perceptron for Breast Cancer Classification

### AIM:
To implement breast tumour classification using medical diagnostic measurements.

### QUESTION:

Develop a binary classification model using the Breast Cancer Wisconsin Diagnostic dataset. Train a perceptron using tumour measurements and classify samples into benign and malignant categories. Evaluate the model using accuracy and a confusion matrix.

### CODE:

```python
import numpy as np

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import Perceptron

from sklearn.pipeline import make_pipeline

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()

X = data.data

y = 1 - data.target

X_train, X_test, y_train, y_test = train_test_split(

    X, y,

    test_size=0.2,

    random_state=42,

    stratify=y

)

model = make_pipeline(

    StandardScaler(),

    Perceptron(

        max_iter=1000,

        eta0=0.1,

        random_state=42

    )

)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print("Breast Cancer Classification Using Perceptron")

print("-----------------------------------------------")

print("Training Samples:", len(X_train))

print("Testing Samples:", len(X_test))

print("\nClassification Accuracy: {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix:")

print(cm)

print("\nClassification Report:")

print(classification_report(

    y_test,

    y_pred,

    target_names=["Benign", "Malignant"]

))

new_sample = X_test[0].reshape(1, -1)

prediction = model.predict(new_sample)

print("New Sample Prediction:",

      "Malignant" if prediction[0] == 1 else "Benign")
```

### OUTPUT:

```text
Breast Cancer Classification Using Perceptron

-----------------------------------------------

Training Samples: 455

Testing Samples: 114

Classification Accuracy: 97.37%

Confusion Matrix:

[[71  1]
 [ 2 40]]

Classification Report:

              precision    recall  f1-score   support

      Benign       0.97      0.99      0.98        72

   Malignant       0.98      0.95      0.96        42

    accuracy                           0.97       114

   macro avg       0.97      0.97      0.97       114

weighted avg       0.97      0.97      0.97       114

New Sample Prediction: Benign
```