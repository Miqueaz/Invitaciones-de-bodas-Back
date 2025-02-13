from flask import Flask, request, jsonify
from openpyxl import Workbook, load_workbook
import os

app = Flask(__name__)

# Ruta al archivo Excel
EXCEL_FILE = 'asistencia.xlsx'

# Verificar si el archivo Excel existe, si no, crearlo
if not os.path.exists(EXCEL_FILE):
    wb = Workbook()
    ws = wb.active
    ws.title = "Asistencia"
    ws.append(['ID', 'Fecha', 'Hora'])
    wb.save(EXCEL_FILE)

@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    # Obtener el ID del cuerpo de la solicitud
    data = request.json
    id_usuario = data.get('id')

    if not id_usuario:
        return jsonify({'error': 'ID no proporcionado'}), 400

    # Cargar el archivo Excel existente
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active

    # Obtener la fecha y hora actual
    from datetime import datetime
    now = datetime.now()
    fecha = now.strftime('%Y-%m-%d')
    hora = now.strftime('%H:%M:%S')

    # Registrar la asistencia en el archivo Excel
    ws.append([id_usuario, fecha, hora])
    wb.save(EXCEL_FILE)

    return jsonify({'mensaje': 'Asistencia registrada correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)