# AI LAB – 4

## EXPERIMENT 16: Naïve Bayes Classification for Wine Classification

### AIM:
To implement wine classification using chemical composition analysis.

### QUESTION:

In the food and beverage industry, laboratory measurements can help identify wine categories based on their chemical properties. A machine learning model can analyse features such as alcohol content, acidity, magnesium and flavonoids to classify wine samples into their respective categories.

Develop a classification system using the Wine Recognition dataset. Train a Gaussian Naïve Bayes model using the chemical measurements of wine samples and predict their respective categories. Evaluate the model using classification accuracy and a confusion matrix.

### CODE:

```python
import numpy as np

from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (

    accuracy_score,

    confusion_matrix,

    classification_report

)

wine = load_wine()

X = wine.data

y = wine.target

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42,

    stratify=y

)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print("Wine Classification Using Naive Bayes")

print("--------------------------------------")

print("Training Samples:", len(X_train))

print("Testing Samples:", len(X_test))

print("\nClassification Accuracy: {:.2f}%".format(

     accuracy * 100

))

print("\nConfusion Matrix:")

print(cm)

print("\nClassification Report:")

print(classification_report(

     y_test,

     y_pred,

     target_names=wine.target_names

))

new_sample = X_test[0].reshape(1, -1)

prediction = model.predict(new_sample)

print("New Sample Prediction:",

      wine.target_names[prediction[0]])
```

### OUTPUT:

```text
Wine Classification Using Naive Bayes

--------------------------------------

Training Samples: 142

Testing Samples: 36

Classification Accuracy: 97.22%

Confusion Matrix:

[[12  0  0]
 [ 1 13  0]
 [ 0  0 10]]

Classification Report:

              precision    recall  f1-score   support

     class_0       0.92      1.00      0.96        12
     class_1       1.00      0.93      0.96        14
     class_2       1.00      1.00      1.00        10

    accuracy                           0.97        36
   macro avg       0.97      0.98      0.97        36
weighted avg       0.97      0.97      0.97        36

New Sample Prediction: class_0
```