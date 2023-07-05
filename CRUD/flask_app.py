import sqlite3
from flask import Flask, jsonify, request

# CONFIGURACION DE BASE DE DATOS
DATABASE = 'vehiculos.db'

# CONEXION A BASE DE  DATOS

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Crear la tabla 'productos' si no existe
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS autos (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        cantidad INTEGER NOT NULL,
        marca VARCHAR(50),
        modelo VARCHAR(50),
        motor VARCHAR(50),
        potencia INTEGER,
        velocidad INTEGER,
        peso FLOAT,
        color VARCHAR(50)
    )
''')
conn.commit()
cursor.close()
conn.close()

# -------------------------------------------------------------------
#             CLASE AUTO
# -------------------------------------------------------------------


class Auto:
    def __init__(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        self.codigo = codigo
        self.cantidad = cantidad
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.potencia = potencia
        self.velocidad = velocidad
        self.peso = peso
        self.color = color

    def modificar(self, nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color):
        self.cantidad = nuevo_cantidad
        self.marca = nuevo_marca
        self.modelo = nuevo_modelo
        self.motor = nuevo_motor
        self.potencia = nuevo_potencia
        self.velocidad = nuevo_velocidad
        self.peso = nuevo_peso
        self.color = nuevo_color


# -------------------------------------------------------------------
#             CLASE STOCK
# -------------------------------------------------------------------
class Stock:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_auto(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        auto_existe = self.buscar_auto(codigo)
        if auto_existe:
            return jsonify({'messate': 'El Auto ya existe en la base de datos'}), 404

        auto_nuevo = Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        sql = f'INSERT INTO autos VALUES ({codigo}, {cantidad}, "{marca}", "{modelo}", "{motor}", {potencia}, {velocidad}, {peso}, "{color}");'
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Auto agregado exitosamente'}), 200

    def buscar_auto(self, buscarpor, valor):
        if buscarpor == "codigo":
            sql = f"SELECT * FROM autos WHERE codigo = {valor};"
        elif buscarpor == "marca":
            sql = f"SELECT * FROM autos WHERE marca = '{valor}';"
        elif buscarpor == "modelo":
            sql = f"SELECT * FROM autos WHERE modelo = '{valor}';"
        elif buscarpor == "motor":
            sql = f"SELECT * FROM autos WHERE motor = '{valor}';"
        elif buscarpor == "color":
            sql = f"SELECT * FROM autos WHERE color = '{valor}';"
        else:
            return None
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return None
    
    def modificar_auto(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        auto = self.buscar_auto(codigo)
        if auto:
            auto.modificar(nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color)
            sql = f'UPDATE autos SET cantidad = {nuevo_cantidad}, marca = "{nuevo_marca}", modelo = "{nuevo_modelo}", motor = "{nuevo_motor}", potencia = {nuevo_potencia}, velocidad = {nuevo_velocidad}, peso = {nuevo_peso}, color = "{nuevo_color}" WHERE codigo = {codigo};'
            self.cursor.execute(sql)
            self.cursor.commit()
            return jsonify({'message': 'Producto modificado exitosamente'}), 200
        return jsonify({'message':'Producto no encontrado'}), 404

    def eliminar_auto(self, codigo):
        sql = f'DELETE FROM autos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Auto eliminado de la Base de Datos'})
        return jsonify({'message':'Auto no encontrado'}), 404

    def listar_stock(self):
        self.cursor.execute("SELECT * FROM autos")
        rows = self.cursor.fetchall()
        autos = []
        for row in rows:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            auto = {'codigo': codigo, 'cantidad': cantidad, 'marca': marca, 'modelo': modelo, 'motor': motor, 'potencia': potencia, 'velocidad': velocidad, 'peso': peso, 'color': color}
            autos.append(auto)
        return jsonify(autos), 200

# -----------------------------------------------
#         DECORADORES FLASK
# -----------------------------------------------
app = Flask(__name__)
stock = Stock()

@app.route('/autos/<campo>/<valor>', methods=['GET'])
def buscar_auto(campo, valor):
    if campo not in ["codigo", "marca", "modelo", "motor", "color"]:
        return jsonify({'message': 'Campo de búsqueda inválido'}), 400

    auto = stock.buscar_auto(campo, valor)
    if auto:
        return jsonify({
            'codigo': auto.codigo,
            'cantidad': auto.cantidad,
            'marca': auto.marca,
            'modelo': auto.modelo,
            'motor': auto.motor,
            'potencia': auto.potencia,
            'velocidad': auto.velocidad,
            'peso': auto.peso,
            'color': auto.color
        }), 200

    return jsonify({'message': 'Auto no encontrado'}), 404

@app.route('/')
def index():
    return render_template('gestion.html')

@app.route('/autos', methods=['GET'])
def obtener_auto():
    return stock.listar_stock()

@app.route('/autos', methods=['POST'])
def agregar_auto():
    codigo = request.json.get('codigo')
    cantidad = request.json.get('cantidad')
    marca = request.json.get('marca')
    modelo = request.json.get('modelo')
    motor = request.json.get('motor')
    potencia = request.json.get('potencia')
    velocidad = request.json.get('velocidad')
    peso = request.json.get('peso')
    color = request.json.get('color')
    return stock.agregar_auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)

@app.route('/autos/<int:codigo>', methods=['PUT'])
def modificar_auto(codigo):
    nuevo_cantidad = request.json.get('cantidad')
    nuevo_marca = request.json.get('marca')
    nuevo_modelo = request.json.get('modelo')
    nuevo_motor = request.json.get('motor')
    nuevo_potencia = request.json.get('potencia')
    nuevo_velocidad = request.json.get('velocidad')
    nuevo_peso = request.json.get('peso')
    nuevo_color = request.json.get('color')
    return stock.modificar_auto(codigo, nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color)

@app.route('/autos/<int:codigo>', methods=['DELETE'])
def eliminar_auto(codigo):
    return stock.eliminar_auto(codigo)

if __name__ == '__main__':
    app.run()