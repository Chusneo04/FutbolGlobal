from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from config import Config
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
CORS(app, supports_credentials=True, origins=['https://futbolglobal-frontend-wr2g.onrender.com'])


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
                resp.set_cookie('usuario', correo, httponly=True, max_age=60*60*24, samesite='None', secure=True)
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
            resp.set_cookie('usuario', correo, httponly=True, max_age=60*60*24, samesite='None', secure=True)
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

@app.route('/añadir_carrito/<id>', methods = ['GET','POST'])
def añadir_carrito(id):
    datos = request.get_json()
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id FROM usuarios WHERE correo = %s', (datos['cookie'],))
    id_cliente = cursor.fetchone()[0]
    cursor.execute('INSERT INTO carrito (id_camiseta, cliente_id, cantidad) VALUES (%s, %s, %s)', (id, id_cliente, datos['cantidad']))
    mysql.connection.commit()
    return jsonify({'mensaje':'Producto añadido al carrito correctamente'})

@app.route('/obtener_carrito/<correo>')
def obtener_carrito(correo):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id FROM usuarios WHERE correo = %s', (correo,))
    id_cliente = cursor.fetchone()
    cursor.execute('SELECT * FROM carrito WHERE cliente_id = %s', (id_cliente,))
    carrito = cursor.fetchall()
    camisetas = []
    for producto in carrito:
        print(carrito)
        cursor.execute('SELECT * FROM camisetas WHERE id = %s', (producto[1],))
        camiseta = cursor.fetchall()
        atributos_camiseta = {'nombre':camiseta[0][2], 'precio':camiseta[0][3], 'imagen':camiseta[0][5], 'cantidad':producto[3]}
        camisetas.append(atributos_camiseta)
    return jsonify(camisetas)

@app.route('/eliminar_carrito', methods = ['DELETE'])
def eliminar_carrito():
    try:

        datos = request.get_json()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id FROM camisetas WHERE nombre = %s ', (datos['nombre'],))
        id_camiseta = cursor.fetchone()[0]
        print(id_camiseta)
        cursor.execute('DELETE FROM carrito WHERE id_camiseta = %s',(id_camiseta,))
        mysql.connection.commit()
        return jsonify({'mensaje':'Producto eliminado correctamente'})
    except:
        return jsonify({'mensaje':'Ha ocurrido un error al eliminar el producto'})
    
@app.route('/comprar', methods = ['DELETE'])
def comprar():
    try:
        datos = request.get_json()
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id FROM usuarios WHERE correo = %s', (datos['correo'],))
        id_usuario = cursor.fetchone()
        cursor.execute('SELECT * FROM carrito WHERE cliente_id = %s', (id_usuario[0],))
        carrito_cliente = cursor.fetchall()
        productos_cliente = []
        for producto in carrito_cliente:
            productos_cliente.append({'id':producto[0], 'id_camiseta':producto[1], 'id_cliente':producto[2], 'cantidad':producto[3]})
            
        for producto in productos_cliente:
            cursor.execute('INSERT INTO pedidos (id_camiseta, cliente_id, cantidad) VALUES (%s, %s, %s)', (producto['id_camiseta'], producto['id_cliente'], producto['cantidad']))
            
        
        cursor.execute('DELETE FROM carrito WHERE cliente_id = %s', (id_usuario, ))
        mysql.connection.commit()

        return jsonify({'mensaje':'Compra realizada correctamente'})
    except Exception as e:
        print(e)
        return jsonify({'mensaje': 'Ha ocurrido un error al realizar la compra'})   


@app.route('/obtener_pedidos/<correo>')
def obtener_pedidos(correo):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id FROM usuarios WHERE correo = %s', (correo,))
    id_cliente = cursor.fetchone()
    cursor.execute('SELECT * FROM pedidos WHERE cliente_id = %s', (id_cliente,))
    pedidos = cursor.fetchall()
    camisetas = []
    for producto in pedidos:
        print(pedidos)
        cursor.execute('SELECT * FROM camisetas WHERE id = %s', (producto[1],))
        camiseta = cursor.fetchall()
        atributos_camiseta = {'nombre':camiseta[0][2], 'precio':camiseta[0][3], 'imagen':camiseta[0][5], 'cantidad':producto[3]}
        camisetas.append(atributos_camiseta)
    return jsonify(camisetas)    

if __name__ == "__main__":
    app.run(debug=True)