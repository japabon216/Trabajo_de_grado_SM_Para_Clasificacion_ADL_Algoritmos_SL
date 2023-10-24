import joblib
import random
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, f1_score, roc_auc_score, roc_curve

def realizar_prediccion(ruta_archivo):
    dataset9 = pd.read_csv(ruta_archivo)
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

    return (prediccion_fila_aleatoria, y_fila_aleatoria)

if __name__ == '__main__':
    # Coloca la ruta del archivo generado en app.py aquí
    resultado = realizar_prediccion('data/ruta_del_archivo_generado_en_app_py.csv')
    print(f"Predicción para la fila aleatoria: {resultado[0]}")
    print(f"Actividad original: {resultado[1]}")
