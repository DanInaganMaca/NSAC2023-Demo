# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ufcx9UX9TjkIMWMFn5O7-nq73LjM5NIp
"""

import glob
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Cargar los datos desde archivos de texto
fn = []
all_data3 = pd.DataFrame()
for f in glob.glob("./Espectros txt/*.txt"):
    df = pd.read_csv(f, header=None, delimiter=' ' )
    all_data3 = pd.concat([all_data3, df], axis=1)
    fn.append(f)
Datamz = all_data3[0] # realciones m/z
Data = all_data3[1] # Intensidades

Data.columns=range(Data.shape[1]) # Aquí le ponemos indices ordenados a las columna de las intensidades
#Datamz.columns=range(Datamz.shape[1])
#Datamz=Data[[0]]
Datamz.tail(194048) # Inspeccionamos los datos de la relación m/z al final para saber hasta donde todos tienen datos, observamos que hasta la fila 32255 hay datos
Data

# Obtener las relaciones m/z y las intensidades
Datamz = all_data3[0]
Data = all_data3.drop(0, axis=1)  # Eliminar la columna de relaciones m/z

Dsna=Datamz[10:194048]
Dsna

D=Dsna.isnull().any() # En la tabla D quedan la información booleana (False or True) si hay o no datos perdidos en cada espectro (muestra)
D

df = D[D[0]==True]
df

Dataint=Data[0:194048]
Dataint

ET= pd.read_excel('etiquetas.xlsx',header=None)
Y1=ET.set_axis(['Clase'], axis=1, inplace=False)
Y1

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder

encoder = OrdinalEncoder()
encoder.fit(Y1[['Clase']])
Y1_code = encoder.transform (Y1[['Clase']])
Y1_code = pd.DataFrame(Y1_code)
Y1_code

import glob
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Load data from text files
fn = []
all_data3 = pd.DataFrame()
for f in glob.glob("./Espectros txt/*.txt"):
    df = pd.read_csv(f, header=None, delimiter=' ')
    all_data3 = pd.concat([all_data3, df], axis=1)
    fn.append(f)

# Assign column names for data
column_names = [f"Sample_{i}" for i in range(all_data3.shape[1])]
all_data3.columns = column_names

# Separate 'realciones m/z' and 'Intensidades'
Datamz = all_data3['Sample_0']
Data = all_data3.drop('Sample_0', axis=1)

# Unsupervised Anomaly Detection using Isolation Forest
outlier_fraction = 0.1  # Expected proportion of outliers
model = IsolationForest(contamination=outlier_fraction, random_state=42)
pred_labels = model.fit_predict(Data)

# Visualize results
plt.figure(figsize=(12, 6))

# Scatter plot of 'Sample_0' and 'Sample_1'
plt.subplot(1, 2, 1)
plt.scatter(Datamz, Data['Sample_1'], c=pred_labels, cmap='viridis', marker='.')
plt.xlabel('Realciones m/z')
plt.ylabel('Intensidades')
plt.title('Scatter Plot with Isolation Forest Labels')

# Anomaly score histogram
plt.subplot(1, 2, 2)
anomaly_scores = -model.decision_function(Data)
plt.hist(anomaly_scores, bins=50, density=True, alpha=0.7, color='blue')
plt.xlabel('Anomaly Score')
plt.ylabel('Density')
plt.title('Anomaly Score Histogram')

plt.tight_layout()
plt.show()

# Create a DataFrame with labels for the samples
labels_df = pd.DataFrame({'Sample': column_names[1:], 'Label': pred_labels})

# Prepare the classification report (assuming you have ground truth labels)
# Load ground truth labels from a file (replace with your actual file)
ground_truth_labels = pd.read_csv("ground_truth_labels.csv", header=None)

# Assuming the ground truth labels are in the second column of the DataFrame
true_labels = ground_truth_labels.iloc[:, 1]

# Classification report for the predicted labels vs. ground truth labels
print(classification_report(true_labels, pred_labels, target_names=['Normal', 'Anomaly']))

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy import stats  # Import the stats module
# Load data from text files (Assuming you've already loaded data like before)
# ... (Same code for loading data as before)

# Separate 'realciones m/z' and 'Intensidades'
Datamz = all_data3['Sample_0']
Data = all_data3.drop('Sample_0', axis=1)

# Generate synthetic labels (+ or -) for demonstration
np.random.seed(42)
labels = np.random.choice(['+', '-'], size=Data.shape[0], p=[0.2, 0.8])

# Combine data and labels into a single DataFrame
data_with_labels = pd.concat([Data, pd.Series(labels, name='Label')], axis=1)

# Data Exploration and Visualization
# ... (Perform descriptive statistics, box plots, histograms, etc.)

# Statistical Tests
positive_data = data_with_labels[data_with_labels['Label'] == '+']
negative_data = data_with_labels[data_with_labels['Label'] == '-']

# Perform t-tests or other statistical tests for each feature
for feature in Data.columns:
    t_statistic, p_value = stats.ttest_ind(positive_data[feature], negative_data[feature])
    print(f"Feature: {feature}, p-value: {p_value}")

# Data Preprocessing
X = Data.values
y = (labels == '+').astype(int)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Dimensionality Reduction with PCA
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Building a Predictive Model (Random Forest Classifier)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_pca, y_train)
y_pred = clf.predict(X_test_pca)

# Model Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['-', '+']))

# Visualization of Model Performance
# ... (Plot ROC curves, precision-recall curves, etc.)

from sklearn.preprocessing import StandardScaler, Normalizer
scaler=StandardScaler()
norma=Normalizer()
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Extraer características y etiquetas

x_scaled = scaler.fit_transform(Dataint)
pca = PCA(n_components=20)  # Número de componentes principales a mantener
pca1=pca.fit(x_scaled.T)
datos_pca = pca.fit_transform(x_scaled.T)

pca=PCA(n_components=20) # Otra opción es hacer pca hasta obtener un mínimo explicado ej.: pca=PCA(.85)
pca1=pca.fit(x_scaled.T) # obtener los componentes principales
datos_pca=pca.transform(x_scaled.T) # convertimos nuestros datos con las nuevas dimensiones de PCA, scores

#out = pca.fit_transform(valtn) # otra opción

# Esta celda es para observar la varianza explicada con 5 componentes, se podría variar a los que se quisiese
print("shape of datos_pca", datos_pca.shape)
expl = pca.explained_variance_ratio_
print(expl)
print('suma:',sum(expl[0:20]))
#Vemos que con 5 componentes tenemos algo mas del 85% de varianza explicada
datos_pca1 = pd.DataFrame(datos_pca) # Convierte los datos pca en un DataFrame
datos_pca1=pd.concat([datos_pca1, Y1] ,axis=1) # Se agrega la columna del tipo de muestra

import seaborn as sns
# Realizar el PCA
pca = PCA(n_components=5)
pca1 = pca.fit(x_scaled.T)
datos_pca = pca.transform(x_scaled.T)

# Obtener la varianza explicada
expl = pca.explained_variance_ratio_
print("Varianza explicada:", expl)
print("Suma de varianza explicada:", sum(expl))

# Crear un DataFrame con los datos PCA y las etiquetas
datos_pca_df = pd.DataFrame(datos_pca, columns=[f"PC{i+1}" for i in range(datos_pca.shape[1])])
datos_pca_df = pd.concat([datos_pca_df, Y1], axis=1)

# Visualizar la varianza explicada
plt.figure(figsize=(10, 6))
sns.barplot(x=np.arange(1, len(expl) + 1), y=expl)
plt.xlabel("Componente Principal")
plt.ylabel("Varianza Explicada")
plt.title("Varianza Explicada por Componente Principal")
plt.show()

# Visualizar los datos PCA en un gráfico de pares con Seaborn
sns.set(style="ticks")
sns.pairplot(datos_pca_df, hue="Clase", diag_kind="kde")
plt.show()

markers = {'si': 'o', 'no': 's'}

# Realizar el PCA con 20 componentes principales
num_components = 8
pca = PCA(n_components=num_components)
pca1 = pca.fit(x_scaled.T)
datos_pca = pca.transform(x_scaled.T)

# Crear un DataFrame con los datos PCA y las etiquetas
componente_columns = [f"Componente Principal {i+1}" for i in range(num_components)]
datos_pca_df = pd.DataFrame(datos_pca, columns=componente_columns)
datos_pca_df["Clase"] = Y1["Clase"]  # Agregar la columna de clase nuevamente

# Crear un gráfico de dispersión con estilo personalizado y colores pastel
plt.figure(figsize=(10, 6))
sns.set_palette("deep")  # Usar paleta de colores pastel

# Crear el gráfico de dispersión utilizando los marcadores y colores
sns.scatterplot(x="Componente Principal 1", y="Componente Principal 2", data=datos_pca_df,
                hue="Clase", style="Clase", markers=markers, s=100)

# Añadir leyenda personalizada


# Añadir título y ajustar estilo general
plt.title(f"Visualización Mejorada de PCA ({num_components} Componentes Principales)")
sns.despine()  # Eliminar bordes no necesarios

plt.show()

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import cross_val_score

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel() , train_size = 0.2, random_state=42,shuffle = True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Aplicación de algoritmo de aprendizaje automático (Logistic Regression)
model = LogisticRegression()
scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print("Cross-Validation Scores:", scores)
print("Mean CV Score:", np.mean(scores))

# 2. Selección de características
selector = SelectKBest(score_func=f_classif, k=10)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)

# 3. Aplicación de algoritmo de aprendizaje automático en características seleccionadas
model_selected = LogisticRegression()
scores_selected = cross_val_score(model_selected, X_train_selected, y_train, cv=5)
print("Cross-Validation Scores (Selected Features):", scores_selected)
print("Mean CV Score (Selected Features):", np.mean(scores_selected))

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import accuracy_score, silhouette_score

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel() , train_size = 0.2, random_state=42,shuffle = True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Aplicación de algoritmo de aprendizaje automático (Logistic Regression)
model_lr = LogisticRegression()
model_lr.fit(X_train_scaled, y_train)
y_pred_lr = model_lr.predict(X_test_scaled)
acc_lr = accuracy_score(y_test, y_pred_lr)

# 2. Random Forest
model_rf = RandomForestClassifier()
model_rf.fit(X_train_scaled, y_train)
y_pred_rf = model_rf.predict(X_test_scaled)
acc_rf = accuracy_score(y_test, y_pred_rf)

# 3. Support Vector Machine (SVM)
model_svm = SVC()
model_svm.fit(X_train_scaled, y_train)
y_pred_svm = model_svm.predict(X_test_scaled)
acc_svm = accuracy_score(y_test, y_pred_svm)

# 4. K-Means (Clustering, sin etiquetas reales)
model_kmeans = KMeans(n_clusters=2)
model_kmeans.fit(X_train_scaled)
silhouette_kmeans = silhouette_score(X_train_scaled, model_kmeans.labels_)


# Resultados
print("Accuracy - Regresión Logística:", acc_lr)
print("Accuracy - Random Forest:", acc_rf)
print("Accuracy - Support Vector Machine (SVM):", acc_svm)
print("Silhouette Score - K-Means:", silhouette_kmeans)

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=42, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Aplicación de algoritmo de aprendizaje automático (Logistic Regression) con ajuste de hiperparámetros
param_grid_lr = {'C': [0.001, 0.01, 0.1, 1, 10]}
grid_lr = GridSearchCV(LogisticRegression(), param_grid_lr, cv=5)
grid_lr.fit(X_train_scaled, y_train)
best_lr = grid_lr.best_estimator_
y_pred_lr = best_lr.predict(X_test_scaled)
acc_lr = accuracy_score(y_test, y_pred_lr)

# 2. Random Forest con ajuste de hiperparámetros
param_grid_rf = {'n_estimators': [50, 100, 200], 'max_depth': [None, 10, 20]}
grid_rf = GridSearchCV(RandomForestClassifier(), param_grid_rf, cv=5)
grid_rf.fit(X_train_scaled, y_train)
best_rf = grid_rf.best_estimator_
y_pred_rf = best_rf.predict(X_test_scaled)
acc_rf = accuracy_score(y_test, y_pred_rf)

# 3. Support Vector Machine (SVM) con ajuste de hiperparámetros
param_grid_svm = {'C': [0.001, 0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid_svm = GridSearchCV(SVC(), param_grid_svm, cv=5)
grid_svm.fit(X_train_scaled, y_train)
best_svm = grid_svm.best_estimator_
y_pred_svm = best_svm.predict(X_test_scaled)
acc_svm = accuracy_score(y_test, y_pred_svm)

# Resultados
print("Accuracy - Regresión Logística:", acc_lr)
print("Best parameters - Regresión Logística:", grid_lr.best_params_)
print("Accuracy - Random Forest:", acc_rf)
print("Best parameters - Random Forest:", grid_rf.best_params_)
print("Accuracy - Support Vector Machine (SVM):", acc_svm)
print("Best parameters - Support Vector Machine (SVM):", grid_svm.best_params_)

# Reporte de clasificación detallado
print("\nClassification Report - Regresión Logística:")
print(classification_report(y_test, y_pred_lr))

print("\nClassification Report - Random Forest:")
print(classification_report(y_test, y_pred_rf))

print("\nClassification Report - Support Vector Machine (SVM):")
print(classification_report(y_test, y_pred_svm))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Cargar y preprocesar tus datos (x_scaled.T y Y1_code)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=643, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definir los parámetros para la búsqueda de hiperparámetros
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'sigmoid'],
    'gamma': ['scale', 'auto', 0.1, 1]
}

# Crear el modelo SVM
model = SVC()

# Realizar la búsqueda de hiperparámetros con validación cruzada
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Obtener el mejor modelo
best_model = grid_search.best_estimator_

# Predecir en los datos de prueba con el mejor modelo
y_pred = best_model.predict(X_test_scaled)

# Calcular el accuracy
acc_svm = accuracy_score(y_test, y_pred)

# Mostrar resultados
print("Best parameters:", grid_search.best_params_)
print("Accuracy - Support Vector Machine (SVM):", acc_svm)
print("Classification Report - Support Vector Machine (SVM):")
print(classification_report(y_test, y_pred))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Cargar y preprocesar tus datos (x_scaled.T y Y1_code)
# ...

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=643, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definir los parámetros para la búsqueda de hiperparámetros
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'sigmoid', 'poly'],
    'gamma': [0.01, 0.1, 1, 10]
}

# Crear el modelo SVM
model = SVC()

# Realizar la búsqueda de hiperparámetros con validación cruzada
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Obtener el mejor modelo
best_model = grid_search.best_estimator_

# Predecir en los datos de prueba con el mejor modelo
y_pred = best_model.predict(X_test_scaled)

# Calcular el accuracy
acc_svm = accuracy_score(y_test, y_pred)

# Mostrar resultados
print("Best parameters:", grid_search.best_params_)
print("Accuracy - Support Vector Machine (SVM):", acc_svm)
print("Classification Report - Support Vector Machine (SVM):")
print(classification_report(y_test, y_pred))

param_grid = [
    {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['linear']},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['poly'], 'degree': [2, 3, 4]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['rbf'], 'gamma': [0.01, 0.1, 1, 10]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['sigmoid']}
]

model = SVC()

# Realizar la búsqueda de hiperparámetros con validación cruzada
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Obtener el mejor modelo
best_model = grid_search.best_estimator_

# Predecir en los datos de prueba con el mejor modelo
y_pred = best_model.predict(X_test_scaled)

# Calcular el accuracy
acc_svm = accuracy_score(y_test, y_pred)

# Mostrar resultados
print("Best parameters:", grid_search.best_params_)
print("Accuracy - Support Vector Machine (SVM):", acc_svm)
print("Classification Report - Support Vector Machine (SVM):")
print(classification_report(y_test, y_pred))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar y preprocesar tus datos (x_scaled.T y Y1_code)
# ...

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=643, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definir los parámetros para la búsqueda de hiperparámetros con diferentes kernels
param_grid = [
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['linear']},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['poly'], 'degree': [2, 3, 4]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['rbf'], 'gamma': [0.01, 0.1, 1, 10]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['sigmoid']}
]

# Crear el modelo SVM
model = SVC()

# Realizar la búsqueda de hiperparámetros con validación cruzada
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Obtener el mejor modelo
best_model = grid_search.best_estimator_

# Predecir en los datos de prueba con el mejor modelo
y_pred = best_model.predict(X_test_scaled)

# Calcular el accuracy
acc_svm = accuracy_score(y_test, y_pred)

# Mostrar resultados SVM
print("SVM - Best parameters:", grid_search.best_params_)
print("SVM - Accuracy:", acc_svm)
print("SVM - Classification Report:")
print(classification_report(y_test, y_pred))

# Probar otro algoritmo - Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=643)
rf_model.fit(X_train_scaled, y_train)
y_pred_rf = rf_model.predict(X_test_scaled)
acc_rf = accuracy_score(y_test, y_pred_rf)

# Mostrar resultados Random Forest
print("Random Forest - Accuracy:", acc_rf)
print("Random Forest - Classification Report:")
print(classification_report(y_test, y_pred_rf))

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Cargar y preprocesar tus datos (x_scaled.T y Y1_code)
# ...

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=643, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Definir los parámetros para la búsqueda de hiperparámetros con diferentes kernels
param_grid = [
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['linear']},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['poly'], 'degree': [2, 3, 4]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['rbf'], 'gamma': [0.01, 0.1, 1, 10]},
    {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'kernel': ['sigmoid']}
]

# Crear el modelo SVM
model = SVC()

# Realizar la búsqueda de hiperparámetros con validación cruzada
grid_search = GridSearchCV(model, param_grid, cv=5)
grid_search.fit(X_train_scaled, y_train)

# Obtener el mejor modelo
best_model = grid_search.best_estimator_

# Evaluación del modelo con validación cruzada
cross_val_scores = cross_val_score(best_model, X_train_scaled, y_train, cv=5)
mean_cross_val_score = np.mean(cross_val_scores)

# Predecir en los datos de prueba con el mejor modelo
y_pred = best_model.predict(X_test_scaled)

# Calcular el accuracy
acc_svm = accuracy_score(y_test, y_pred)

# Mostrar resultados SVM
print("SVM - Best parameters:", grid_search.best_params_)
print("SVM - Accuracy:", acc_svm)
print("SVM - Mean Cross-Validation Score:", mean_cross_val_score)
print("SVM - Classification Report:")
print(classification_report(y_test, y_pred))

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generar datos de ejemplo
X, y = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, random_state=643)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=643)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo SVM
model = SVC(kernel='linear')
model.fit(X_train_scaled, y_train)

# Predicciones en el conjunto de prueba
y_pred = model.predict(X_test_scaled)

# Graficar los puntos de datos y las predicciones del modelo
plt.figure(figsize=(10, 6))

# Graficar los puntos de datos en función de sus clases reales
plt.scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], c=y_test, cmap='coolwarm', marker='o', label='Real')

# Graficar las predicciones del modelo en función de sus clases predichas
plt.scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], c=y_pred, cmap='coolwarm', marker='x', s=80, label='Predicted')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter Plot of Real vs Predicted Labels')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, roc_auc_score, auc

# Cargar y preprocesar tus datos (x_scaled.T y Y1_code)
# ...

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=643, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo SVM con kernel polinómico de grado 3
model = SVC(kernel='poly', degree=3)
model.fit(X_train_scaled, y_train)

# Predecir probabilidades en lugar de clases para la curva ROC
y_probs = model.decision_function(X_test_scaled)

# Calcular la curva ROC y el AUC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

# Crear el gráfico de la curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) - Polynomial Kernel (Degree 3)')
plt.legend(loc="lower right")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Supongamos que tienes X_train_scaled, X_test_scaled, y_train, y_test

# Identifica las etiquetas únicas en y_train
unique_labels = np.unique(y_train)

# Elige un ejemplo de cada grupo para visualizar
examples_to_visualize = 2

plt.figure(figsize=(12, 6 * examples_to_visualize))

for i, label in enumerate(unique_labels):
    # Encuentra los índices de ejemplos con la etiqueta actual
    indices = np.where(y_train == label)[0]

    # Elije algunos ejemplos al azar para visualizar
    chosen_indices = np.random.choice(indices, examples_to_visualize, replace=False)

    for j, index in enumerate(chosen_indices):
        plt.subplot(len(unique_labels), examples_to_visualize, i * examples_to_visualize + j + 1)
        plt.plot(X_train_scaled[index])
        plt.title(f'Label: {label}')

plt.tight_layout()
plt.show()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=42, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Selección de características utilizando ANOVA
selector = SelectKBest(score_func=f_classif, k=10)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)

# Entrenar un modelo de regresión logística
model_lr = LogisticRegression()
model_lr.fit(X_train_selected, y_train)

# Obtener los coeficientes del modelo
coeficients = model_lr.coef_[0]

# Crear un DataFrame con los coeficientes y las características
features = ["Feature_" + str(i) for i in range(X_train_selected.shape[1])]
coef_df = pd.DataFrame({"Feature": features, "Coefficient": coeficients})

# Ordenar por valor absoluto de los coeficientes
coef_df["Abs_Coefficient"] = np.abs(coef_df["Coefficient"])
coef_df = coef_df.sort_values(by="Abs_Coefficient", ascending=False)

# Mostrar la tabla con los coeficientes y las características
print(coef_df)

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif

# Generar valores ficticios de m/z en un rango de 500 a 6000
num_features = 10  # Número de características seleccionadas
min_mz = 500
max_mz = 6000
mz_values = np.linspace(min_mz, max_mz, num_features)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x_scaled.T, Y1_code.values.ravel(), train_size=0.8, random_state=42, shuffle=True)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Selección de características utilizando ANOVA
selector = SelectKBest(score_func=f_classif, k=num_features)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)

# Obtener los coeficientes del modelo
coeficients = model_lr.coef_[0]

# Crear un DataFrame con los coeficientes y las características
features = ["Feature_" + str(i) for i in range(X_train_selected.shape[1])]
coef_df = pd.DataFrame({"Feature": features, "Coefficient": coeficients, "m/z": mz_values})

# Ordenar por valor absoluto de los coeficientes
coef_df["Abs_Coefficient"] = np.abs(coef_df["Coefficient"])
coef_df = coef_df.sort_values(by="Abs_Coefficient", ascending=False)

# Mostrar la tabla con los coeficientes, características y valores de m/z
print(coef_df)

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

# Cargar y preparar los datos y etiquetas como mencionaste
# ...

# Dividir los datos en grupos según las etiquetas
data_positivos = x_scaled.T[Y1_code.values.ravel() == 1]
data_sanos = x_scaled.T[Y1_code.values.ravel() == 0]

