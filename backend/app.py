from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from config import Config
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
CORS(app, supports_credentials=True)


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

@app.route('/obtener-camisetas/<liga>')
def obtener_camisetas(liga):
    print('Liga: ', liga)
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM camisetas INNER JOIN equipos ON camisetas.id_equipo = equipos.id WHERE equipos.liga = %s', (liga,))
    resultados = cursor.fetchall()
    print(resultados)
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
    print(camisetas)
    return jsonify(camisetas)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        correo = data.get('correo')
        clave = data.get('clave')
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
        usuario_existente = cursor.fetchone()
        if usuario_existente:
            if check_password_hash(usuario_existente[3], clave):
                resp = make_response(jsonify({'mensaje': 'Bienvenido {}'.format(usuario_existente[1])})) 
                resp.set_cookie('usuario', correo, httponly=False, max_age=60*60*24)
                return resp
            return jsonify({'mensaje':'Las credenciales introducidas son incorrectas'})
        return jsonify({'mensaje':'El usuario no existe'})
    
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        datos = request.get_json()
        
        nombre = datos.get('nombre')
        correo = datos.get('correo')
        clave = datos.get('clave')
        clave = generate_password_hash(clave)
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
        usuario_existe = cursor.fetchone()
        print(usuario_existe)
        if usuario_existe:
            return jsonify({'mensaje':'El usuario ya existe'})
        else:
            cursor.execute('INSERT INTO usuarios (nombre, correo, clave) VALUES (%s, %s, %s)', (nombre, correo, clave))
            mysql.connection.commit()
            cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
            usuario = cursor.fetchone()
            resp = make_response(jsonify({'mensaje': 'Bienvenido {}'.format(usuario[1])})) 
            resp.set_cookie('usuario', correo, httponly=True, max_age=60*60*24)
            return resp

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    if request.method == 'POST':
        resp = make_response(jsonify({'mensaje':'Sesion Cerrada'}))
        resp.set_cookie('usuario', expires=0)
        return resp

@app.route('/obtener-usuario/<correo>')
def obtener_usuario(correo):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = %s', (correo,))
    usuario_obtenido = cursor.fetchone()
    usuario = {}
    usuario['nombre'] = usuario_obtenido[1]
    usuario['correo'] = usuario_obtenido[2]

    return usuario

if __name__ == "__main__":
    app.run(debug=True)