import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train_images = train_images/255.0
# test_images = test_images/255.0

# model = keras.Sequential([
# 	keras.layers.Flatten(input_shape=(28,28)),
# 	keras.layers.Dense(128, activation="relu"),
# 	keras.layers.Dense(10, activation="softmax")
# 	])

# model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# model.fit(train_images, train_labels, epochs=10)

# test_loss, test_acc = model.evaluate(test_images, test_labels)

# print('\nTest accuracy:', test_acc)

# model.save("model.h5")
model = keras.models.load_model("model.h5")

predictions = model.predict(test_images)
plt.figure(figsize=(5,5))
for i in range(10, 15):
    plt.grid(False)
    plt.imshow(test_images[i])
    plt.xlabel(class_names[test_labels[i]])
    plt.title(class_names[np.argmax(predictions[i])])
    plt.show()
