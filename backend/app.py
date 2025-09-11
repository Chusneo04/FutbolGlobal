from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import Config
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
CORS(app)


@app.route('/obtener_equipos/<liga>', methods = ['GET', 'POST'])
def index(liga):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM equipos WHERE liga = %s', (liga,))
    resultados = cursor.fetchall()
    equipos = []
    for fila in resultados:
        equipos.append({
            'id': fila[0],
            'nombre': fila[1],
            'liga': fila[2],
            'imagen':fila[3]
        })
    
    
    return jsonify(equipos)
    

@app.route('/obtener-camisetas-aleatorias')
def obtener_camisetas_aleatorias():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM camisetas ORDER BY RAND() LIMIT 3')
    resultados = cursor.fetchall()
    
    
    camisetas = []
    for fila in resultados:
        camisetas.append({
            'id': fila[0],
            'id_equipo': fila[1],
            'nombre': fila[2],
            'precio': fila[3],
            'stock': fila[4],
            'imagen': fila[5]
        })
    return jsonify(camisetas)

if __name__ == "__main__":
    app.run(debug=True)