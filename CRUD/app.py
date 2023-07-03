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


