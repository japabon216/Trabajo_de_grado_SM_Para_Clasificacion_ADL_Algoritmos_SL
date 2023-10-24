from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pandas as pd
from app_caracteristicas import Calculo_de_caracteristicas
import modelo  # Importa el archivo modelo.py

app = Flask(__name__)
app.secret_key = 'hola'  # Cambia 'your_secret_key' por tu clave secreta

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generar_data_existente', methods=['GET'])
def generar_data_existente():
    try:
        # Es importante que el dataset que se lea aquí ya haya pasado por las características
        dataset_path = 'data/Dataset_Prueba_Caracteristicas.csv'
        
    
                
        # Puedes guardar el resultado en un archivo si es necesario
   
        session['resultado_path'] = dataset_path

        response = {"message": "Datos generados con éxito utilizando el dataset existente."}
        return jsonify(response)
    except Exception as e:
        response = {"error": f"Error al generar datos con el dataset existente: {str(e)}"}
        return jsonify(response), 500


@app.route('/subir_archivo_csv', methods=['POST'])
def subir_archivo_csv():
    try:
        file = request.files['file']
        if file:
            file_name = file.filename
            new_file_name = file_name.split('.')[0] + '_caracteristicas.csv'
            df = pd.read_csv(file)
            resultado = Calculo_de_caracteristicas(df=df, filas_por_grupo=500)
            resultado_path = f'data/{new_file_name}'  # Guarda la ruta del archivo generado
            resultado.to_csv(resultado_path, index=False)
            session['resultado_path'] = resultado_path  # Almacena la ruta en una variable de sesión
            response = {"message": f"Archivo CSV cargado y procesado con éxito. Nombre del archivo generado: {new_file_name}"}
            return jsonify(response)
        else:
            response = {"error": "No se ha seleccionado un archivo CSV."}
            return jsonify(response), 400
    except Exception as e:
        response = {"error": f"Error al procesar el archivo CSV: {str(e)}"}
        return jsonify(response), 500

@app.route('/predecir_actividad')
def predecir_actividad():
    try:
        # Obtiene la ruta del archivo generado desde la variable de sesión
        resultado_path = session.get('resultado_path')
        print(resultado_path)
        if resultado_path:
            resultado_prediccion = modelo.realizar_prediccion(resultado_path)
            
            # Diccionario de mapeo de actividades
            mapeo_actividades = {
                6: "Caminando",
                16: "Estar Sentado",
                17: "Estar De Pie",
                18: "Estar Acostado"
            }
            
            # Obtiene las actividades predecida y a predecir
            actividad_predecida = mapeo_actividades.get(resultado_prediccion[0], "Desconocida")
            actividad_a_predecir = mapeo_actividades.get(resultado_prediccion[1], "Desconocida")
            print(actividad_predecida)
            print(actividad_a_predecir)
            return render_template('result.html', actividad_predecida=actividad_predecida, actividad_a_predecir=actividad_a_predecir)
        else:
            return "No se ha procesado un archivo CSV aún."
    except Exception as e:
        return f"Error al realizar la predicción: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)