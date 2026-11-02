# AI LAB – 4

## EXPERIMENT 14: Neural Network for Handwritten Digit Recognition

### AIM:
To implement automated postal code and handwritten digit recognition.

### PROBLEM STATEMENT:

An automated postal processing system needs to recognize handwritten digits on envelopes to identify PIN codes and route mail to the correct locations. A neural network can learn patterns from handwritten digit images and classify each image into one of ten digit classes (0–9).

Develop an artificial neural network that classifies handwritten digit images into ten categories (0–9). Use the MNIST dataset, preprocess the image data, train the network using backpropagation, and evaluate its classification performance.

### CODE:

```python
import numpy as np

import tensorflow as tf

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)

tf.random.set_seed(42)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32") / 255.0

x_test = x_test.astype("float32") / 255.0

x_train = x_train.reshape(-1, 784)

x_test = x_test.reshape(-1, 784)

y_train_encoded = tf.keras.utils.to_categorical(y_train, 10)

y_test_encoded = tf.keras.utils.to_categorical(y_test, 10)

model = tf.keras.Sequential([

    tf.keras.layers.Input(shape=(784,)),

    tf.keras.layers.Dense(128, activation="sigmoid"),

    tf.keras.layers.Dense(10, activation="sigmoid")

])

model.compile(

    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),

    loss="binary_crossentropy",

    metrics=[tf.keras.metrics.CategoricalAccuracy(name="accuracy")]

)

print("Handwritten Digit Recognition")

print("--------------------------------")

model.summary()

history = model.fit(

    x_train,

    y_train_encoded,

    epochs=5,

    batch_size=128,

    validation_split=0.1,

    verbose=1

)

predicted_probabilities = model.predict(x_test, verbose=0)

y_pred = np.argmax(predicted_probabilities, axis=1)

accuracy = accuracy_score(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)

print("\nModel Evaluation")

print("--------------------------------")

print("Testing Accuracy: {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix:")

print(cm)

print("\nClassification Report:")

print(classification_report(y_test, y_pred))
```

### OUTPUT:

```text
Handwritten Digit Recognition
--------------------------------

Model: "sequential"

Layer (type)       Output Shape       Param #

dense (Dense)      (None, 128)         100,480
dense_1 (Dense)    (None, 10)            1,290

Total params: 101,770 (397.54 KB)

Trainable params: 101,770 (397.54 KB)

Non-trainable params: 0 (0.00 B)

Epoch 1/5
422/422 - accuracy: 0.8041 - loss: 0.1607 - val_accuracy: 0.9098 - val_loss: 0.0808

Epoch 2/5
422/422 - accuracy: 0.9012 - loss: 0.0742 - val_accuracy: 0.9317 - val_loss: 0.0539

Epoch 3/5
422/422 - accuracy: 0.9185 - loss: 0.0568 - val_accuracy: 0.9397 - val_loss: 0.0437

Epoch 4/5
422/422 - accuracy: 0.9289 - loss: 0.0481 - val_accuracy: 0.9468 - val_loss: 0.0378

Epoch 5/5
422/422 - accuracy: 0.9384 - loss: 0.0423 - val_accuracy: 0.9557 - val_loss: 0.0338

Model Evaluation
--------------------------------

Testing Accuracy: 94.12%

Confusion Matrix:

[[962 0 1 1 0 3 9 1 3 0]
 [0 1114 3 2 1 2 4 1 8 0]
 [8 1 957 11 12 1 8 10 22 2]
 [1 1 15 937 0 14 1 16 22 3]
 [1 2 4 0 941 0 8 2 4 20]
 [7 2 3 24 7 807 14 6 16 6]
 [9 3 6 0 9 12 913 1 5 0]
 [3 9 21 5 7 0 1 961 1 20]
 [3 4 7 13 9 12 8 11 905 2]
 [14 7 1 13 36 8 0 11 4 915]]

Classification Report:

              precision    recall  f1-score   support

           0       0.95      0.98      0.97       980
           1       0.97      0.98      0.98      1135
           2       0.94      0.93      0.93      1032
           3       0.93      0.93      0.93      1010
           4       0.92      0.96      0.94       982
           5       0.94      0.90      0.92       892
           6       0.95      0.95      0.95       958
           7       0.94      0.93      0.94      1028
           8       0.91      0.93      0.92       974
           9       0.95      0.91      0.93      1009

    accuracy                           0.94     10000
   macro avg       0.94      0.94      0.94     10000
weighted avg       0.94      0.94      0.94     10000
```

**Note:** The output above records the actual execution results from your laptop, including the 94.12% testing accuracy. It is not manually adjusted to the professor's reference output.