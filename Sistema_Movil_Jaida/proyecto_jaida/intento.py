import joblib
from sklearn.metrics import accuracy_score, precision_score, f1_score, roc_auc_score, roc_curve
import random
import pandas as pd
dataset9 = pd.read_csv('data/Dataset_9_normalizado_4_actividades_caracteristicas.csv')
modelo = joblib.load('Random_Forest_5_Actividades.pkl')


# Escoge un índice aleatorio del conjunto de datos
indice_aleatorio = random.randint(0, len(dataset9) - 1)

# Obtén la fila correspondiente al índice aleatorio
fila_aleatoria = dataset9.iloc[indice_aleatorio, :]

# Extrae las características de la fila
X_fila_aleatoria = fila_aleatoria.drop("Activity")
y_fila_aleatoria = fila_aleatoria["Activity"]

# Realiza la predicción para esta fila
prediccion_fila_aleatoria = modelo.predict([X_fila_aleatoria])[0]

print(f"Predicción para la fila aleatoria: {prediccion_fila_aleatoria}")
print(f"PActividad original: {prediccion_fila_aleatoria}")