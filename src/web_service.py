import csv
from flask import Flask, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/', methods=['GET'])
def generar_json():
    ruta_archivo_csv = 'data/employees.csv'
    data = []
    with open(ruta_archivo_csv, 'r') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for linea in lector:
            data.append(linea)
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host = "0.0.0.0", port = "5050")
