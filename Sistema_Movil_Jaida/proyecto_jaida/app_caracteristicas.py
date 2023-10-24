import pandas as pd
import numpy as np

def calcular_entropia(datos):
    # Calcular las probabilidades de ocurrencia de cada valor
    unique_values, value_counts = np.unique(datos, return_counts=True)
    probabilities = value_counts / len(datos)

    # Calcular la entropía usando la fórmula de Shannon
    entropia = -np.sum(probabilities * np.log2(probabilities))

    return entropia

def promedio_absoluto(segmento):
    return segmento.abs().mean()

def calcular_promedio_resultante(segmento):
    sumatoria = np.sum(np.sqrt(segmento['X_Acc']**2 + segmento['Y_Acc']**2 + segmento['Z_Acc']**2))
    promedio = sumatoria / len(segmento)
    return promedio

def calcular_energia(segmento):
    sumatoria = np.sum(np.sqrt(segmento['X_Acc']**2 + segmento['Y_Acc']**2 + segmento['Z_Acc']**2))
    return sumatoria

def calcular_promedio_resultante_gyro(segmento):
    sumatoria = np.sum(np.sqrt(segmento['X_Gyro']**2 + segmento['Y_Gyro']**2 + segmento['Z_Gyro']**2))
    promedio = sumatoria / len(segmento)
    return promedio

def calcular_energia_gyro(segmento):
    sumatoria = np.sum(np.sqrt(segmento['X_Gyro']**2 + segmento['Y_Gyro']**2 + segmento['Z_Gyro']**2))
    return sumatoria

def Calculo_de_caracteristicas(df, filas_por_grupo=500):
    total_grupos = len(df) // filas_por_grupo
    resultados = pd.DataFrame()

    for i in range(total_grupos):
        inicio = i * filas_por_grupo
        fin = (i + 1) * filas_por_grupo
        resultado_fila = {}
        grupo = df.iloc[inicio:fin]

        for columna in ['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']:
            resultado_fila[f'{columna}_entropy'] = calcular_entropia(grupo[columna])

        promedios = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].mean()
        resultado_fila.update({
            'Activity': grupo['Activity'].iloc[0],
            'Code': grupo['Code'].iloc[0],
            'X_Acc_mean': promedios['X_Acc'],
            'Y_Acc_mean': promedios['Y_Acc'],
            'Z_Acc_mean': promedios['Z_Acc'],
            'X_Gyro_mean': promedios['X_Gyro'],
            'Y_Gyro_mean': promedios['Y_Gyro'],
            'Z_Gyro_mean': promedios['Z_Gyro']
        })

        std_deviation = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].std()
        resultado_fila.update({
            'X_Acc_std': std_deviation['X_Acc'],
            'Y_Acc_std': std_deviation['Y_Acc'],
            'Z_Acc_std': std_deviation['Z_Acc'],
            'X_Gyro_std': std_deviation['X_Gyro'],
            'Y_Gyro_std': std_deviation['Y_Gyro'],
            'Z_Gyro_std': std_deviation['Z_Gyro']
        })

        median_values = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].median()
        resultado_fila.update({
            'X_Acc_50': median_values['X_Acc'],
            'Y_Acc_50': median_values['Y_Acc'],
            'Z_Acc_50': median_values['Z_Acc'],
            'X_Gyro_50': median_values['X_Gyro'],
            'Y_Gyro_50': median_values['Y_Gyro'],
            'Z_Gyro_50': median_values['Z_Gyro']
        })

        max_values = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].max()
        resultado_fila.update({
            'X_Acc_max': max_values['X_Acc'],
            'Y_Acc_max': max_values['Y_Acc'],
            'Z_Acc_max': max_values['Z_Acc'],
            'X_Gyro_max': max_values['X_Gyro'],
            'Y_Gyro_max': max_values['Y_Gyro'],
            'Z_Gyro_max': max_values['Z_Gyro']
        })

        min_values = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].min()
        resultado_fila.update({
            'X_Acc_min': min_values['X_Acc'],
            'Y_Acc_min': min_values['Y_Acc'],
            'Z_Acc_min': min_values['Z_Acc'],
            'X_Gyro_min': min_values['X_Gyro'],
            'Y_Gyro_min': min_values['Y_Gyro'],
            'Z_Gyro_min': min_values['Z_Gyro']
        })

        promedio_absoluto_values = grupo[['X_Acc', 'Y_Acc', 'Z_Acc', 'X_Gyro', 'Y_Gyro', 'Z_Gyro']].apply(promedio_absoluto)
        resultado_fila.update({
            'X_Acc_abslt': promedio_absoluto_values['X_Acc'],
            'Y_Acc_abslt': promedio_absoluto_values['Y_Acc'],
            'Z_Acc_abslt': promedio_absoluto_values['Z_Acc'],
            'X_Gyro_abslt': promedio_absoluto_values['X_Gyro'],
            'Y_Gyro_abslt': promedio_absoluto_values['Y_Gyro'],
            'Z_Gyro_abslt': promedio_absoluto_values['Z_Gyro']
        })

        promedio_resultante_Acc = calcular_promedio_resultante(grupo[['X_Acc', 'Y_Acc', 'Z_Acc']])
        resultado_fila['promedio_resultante_Acc'] = promedio_resultante_Acc

        energia_Acc = calcular_energia(grupo[['X_Acc', 'Y_Acc', 'Z_Acc']])
        resultado_fila['energia_Acc'] = energia_Acc

        promedio_resultante_Gyro = calcular_promedio_resultante_gyro(grupo[['X_Gyro', 'Y_Gyro', 'Z_Gyro']])
        resultado_fila['promedio_resultante_Gyro'] = promedio_resultante_Gyro

        energia_Gyro = calcular_energia_gyro(grupo[['X_Gyro', 'Y_Gyro', 'Z_Gyro']])
        resultado_fila['energia_Gyro'] = energia_Gyro

        resultados = pd.concat([resultados, pd.DataFrame([resultado_fila])], ignore_index=True)

    resultados = resultados[['Activity','Code', 'X_Acc_entropy', 'Y_Acc_entropy', 'Z_Acc_entropy', 'X_Gyro_entropy', 'Y_Gyro_entropy', 'Z_Gyro_entropy', 'X_Acc_mean', 'Y_Acc_mean', 'Z_Acc_mean', 'X_Gyro_mean', 'Y_Gyro_mean', 'Z_Gyro_mean', 'X_Acc_std', 'Y_Acc_std', 'Z_Acc_std', 'X_Gyro_std', 'Y_Gyro_std', 'Z_Gyro_std', 'X_Acc_50', 'Y_Acc_50', 'Z_Acc_50', 'X_Gyro_50', 'Y_Gyro_50', 'Z_Gyro_50', 'X_Acc_max', 'Y_Acc_max', 'Z_Acc_max', 'X_Gyro_max', 'Y_Gyro_max', 'Z_Gyro_max', 'X_Acc_min', 'Y_Acc_min', 'Z_Acc_min', 'X_Gyro_min', 'Y_Gyro_min', 'Z_Gyro_min', 'X_Acc_abslt', 'Y_Acc_abslt', 'Z_Acc_abslt', 'X_Gyro_abslt', 'Y_Gyro_abslt', 'Z_Gyro_abslt', 'promedio_resultante_Acc', 'promedio_resultante_Gyro', 'energia_Acc', 'energia_Gyro']]

    resultados['Code'] = resultados['Code'].astype(str)

    # Crear tres nuevas columnas vacías en el DataFrame
    resultados['Sensor_Type'] = ''
    resultados['Left_Right'] = ''
    resultados['Ubication'] = ''

    # Utilizar el método str.slice para separar los dígitos y asignarlos a las nuevas columnas
    resultados['Sensor_Type'] = resultados['Code'].str.slice(0, 1)
    resultados['Left_Right'] = resultados['Code'].str.slice(1, 2)
    resultados['Ubication'] = resultados['Code'].str.slice(2, 3)

    resultados.drop(columns=['Code'], inplace=True)

    # Convertir las nuevas columnas a tipo int
    resultados['Sensor_Type'] = resultados['Sensor_Type'].astype(int)
    resultados['Left_Right'] = resultados['Left_Right'].astype(int)
    resultados['Ubication'] = resultados['Ubication'].astype(int)
    resultados['Activity'] = resultados['Activity'].astype(int)

    resultados = resultados.reindex(columns=['Activity','X_Acc_std', 'Y_Acc_std', 'Z_Acc_std', 'X_Gyro_std',
          'Y_Gyro_std', 'Z_Gyro_std', 'X_Acc_mean', 'Y_Acc_mean', 'Z_Acc_mean',
          'X_Gyro_mean', 'Y_Gyro_mean', 'Z_Gyro_mean', 'X_Acc_50', 'Y_Acc_50',
          'Z_Acc_50', 'X_Gyro_50', 'Y_Gyro_50', 'Z_Gyro_50', 'X_Acc_max',
          'Y_Acc_max', 'Z_Acc_max', 'X_Gyro_max', 'Y_Gyro_max', 'Z_Gyro_max',
          'X_Acc_min', 'Y_Acc_min', 'Z_Acc_min', 'X_Gyro_min', 'Y_Gyro_min',
          'Z_Gyro_min', 'promedio_resultante_Acc', 'promedio_resultante_Gyro',
          'energia_Acc', 'energia_Gyro', 'X_Acc_abslt', 'Y_Acc_abslt',
          'Z_Acc_abslt', 'X_Gyro_abslt', 'Y_Gyro_abslt', 'Z_Gyro_abslt',
          'X_Acc_entropy', 'Y_Acc_entropy', 'Z_Acc_entropy', 'X_Gyro_entropy',
          'Y_Gyro_entropy', 'Z_Gyro_entropy', 'Sensor_Type', 'Left_Right',
          'Ubication'])

    return resultados
