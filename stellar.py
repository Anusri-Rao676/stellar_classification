# -*- coding: utf-8 -*-
"""stellar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AVNV39UlE1tNGbP5FLyTDDUXKx0l4QET
"""

!pip install pandas scikit-learn matplotlib seaborn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#import the dataset
from google.colab import files
uploaded = files.upload()

data = pd.read_csv(list(uploaded.keys())[0])

#checking if the dataset has been imported properly
print(data.head())

print(data.info())

#identifying features
features = ['u', 'g', 'r', 'i', 'z', 'redshift']

X = data[features]

y = data['class']

#assigning categorical values [0-> star 1->galaxy 2->quasar]
y = y.astype('category').cat.codes

#training the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm_model = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)

svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)

print("SVM Classification Report:")
print(classification_report(y_test, y_pred_svm))

print("k-NN Classification Report:")
print(classification_report(y_test, y_pred_knn))

#plotting the confusion matrix
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.heatmap(confusion_matrix(y_test, y_pred_svm), annot=True, fmt="d", ax=axes[0], cmap="Blues")
axes[0].set_title("SVM Confusion Matrix")
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt="d", ax=axes[1], cmap="Greens")
axes[1].set_title("k-NN Confusion Matrix")
plt.show()

accuracy_svm = accuracy_score(y_test, y_pred_svm)
accuracy_knn = accuracy_score(y_test, y_pred_knn)

print(f"SVM Accuracy: {accuracy_svm:.2f}")
print(f"k-NN Accuracy: {accuracy_knn:.2f}")
