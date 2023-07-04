import sqlite3

# Configurar la conexión a la base de datos SQLite
DATABASE = 'vehiculos.db'

# Obtener la conexión a la base de datos
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
# Definimos la clase "Auto"
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

    def modificar(self, nuevo_codigo, nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color):
        self.codigo = nuevo_codigo
        self.cantidad = nuevo_cantidad
        self.marca = nuevo_marca
        self.modelo = nuevo_modelo
        self.motor = nuevo_motor
        self.potencia = nuevo_potencia
        self.velocidad = nuevo_velocidad
        self.peso = nuevo_peso
        self.color = nuevo_color


# -------------------------------------------------------------------
# Definimos la clase "Stock"
# -------------------------------------------------------------------
class Stock:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_auto(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        auto_existe = self.consultar_auto_codigo(codigo)
        if auto_existe:
            print("El auto ya existe en la Base de Datos")
            return False

        auto_nuevo = Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        sql = f'INSERT INTO autos VALUES ({codigo}, {cantidad}, "{marca}", "{modelo}", "{motor}", {potencia}, {velocidad}, {peso}, "{color}");'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True

    def consultar_auto_codigo(self, codigo):
        sql = f'SELECT * FROM autos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    def consultar_auto_marca(self, marca):
        sql = f'SELECT * FROM autos WHERE marca = "{marca}";'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    def consultar_auto_modelo(self, modelo):
        sql = f'SELECT * FROM autos WHERE modelo = "{modelo}";'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    def consultar_auto_motor(self, motor):
        sql = f'SELECT * FROM autos WHERE motor = "{motor}";'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    def consultar_auto_color(self, color):
        sql = f'SELECT * FROM autos WHERE color = "{color}";'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    def modificar_auto(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        auto = self.consultar_auto_codigo(codigo)
        if auto:
            auto.modificar(nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color)
            sql = f'UPDATE autos SET cantidad = {nuevo_cantidad}, marca = "{nuevo_marca}", modelo = "{nuevo_modelo}", motor = "{nuevo_motor}", potencia = {nuevo_potencia}, velocidad = {nuevo_velocidad}, peso = {nuevo_peso}, color = "{nuevo_color}" WHERE codigo = {codigo};'
            self.cursor.execute(sql)
            self.cursor.commit()
    
    def eliminar_auto(self, codigo):
        sql = f'DELETE FROM autos WHERE codigo = {codigo};'
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            print(f'Auto código: "{codigo}" eliminado')
            self.conexion.commit()
        else:
            print(f'Auto código "{codigo}" no encontrado')
    
    def listar_stock(self):
        self.cursor.execute("SELECT * FROM autos")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            print(f'{codigo}, {cantidad}, {marca}, {modelo}, {motor}, {potencia}, {velocidad}, {peso}, {color}')
        



# -----------------------------------------------------------------------
#             PRUEBAS
# -----------------------------------------------------------------------
# manejador = Stock()

# nuevo_auto = manejador.agregar_auto(1, 2, "Ford", "Mustang", "V10", 460, 138, 1690, "Negro")

# consulta = manejador.consultar_auto_codigo(1)
# print(f'El código del auto es: {consulta.codigo}')

# consulta = manejador.consultar_auto_marca("Ford")
# print(f'La marca del auto es: {consulta.marca}')
# print(f'El modelo del auto es: {consulta.modelo}')
# print(f'El motor del auto es: {consulta.motor}')
# print(f'El color del auto es: {consulta.color}')

# consulta = manejador.consultar_auto_modelo("Mustang")
# print(f'El modelo del auto es: {consulta.modelo}')

# consulta = manejador.consultar_auto_motor("V10")
# print(f'El motor del auto es: {consulta.motor}')

# consulta = manejador.consultar_auto_color("Negro")
# print(f'El color del auto es: {consulta.color}')

# manejador.listar_stock()

# #eliminar_auto = manejador.eliminar_auto(1)

