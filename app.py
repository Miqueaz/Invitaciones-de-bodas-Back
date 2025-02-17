from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar Flask-CORS
import os
import csv
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Ruta al archivo CSV
EXCEL_FILE = 'asistencia.csv'

# Verificar si el archivo CSV existe, si no, crearlo
if not os.path.exists(EXCEL_FILE):
    with open(EXCEL_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir los encabezados
        writer.writerow(['ID', 'Fecha', 'Hora'])

@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    try:
        # Verificar que la solicitud tenga JSON válido
        if not request.is_json:
            return jsonify({'error': 'La solicitud debe ser en formato JSON'}), 400

        # Obtener el ID del cuerpo de la solicitud
        data = request.json
        id_usuario = data.get('id')

        if not id_usuario:
            return jsonify({'error': 'ID no proporcionado'}), 400

        # Obtener la fecha y hora actual
        now = datetime.now()
        fecha = now.strftime('%Y-%m-%d')
        hora = now.strftime('%H:%M:%S')

        # Registrar la asistencia en el archivo CSV
        with open(EXCEL_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_usuario, fecha, hora])  # Escribir nueva línea con asistencia

        return jsonify({'mensaje': 'Asistencia registrada correctamente'}), 200

    except Exception as e:
        # Manejar cualquier error inesperado
        return jsonify({'error': f'Error del servidor: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
