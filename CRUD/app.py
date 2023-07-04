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


class Stock:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_auto(self, codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            print("Producto existente")
            return False
        
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", ( codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color))
        self.conexion.commit()
        return True
    

    # Busqueda de producto por motor

    def consultar_producto_codigo(self, motor):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (motor,))
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color= row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    # Busqueda de producto por marca

    def consultar_producto_codigo(self, marca):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (marca,))
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color= row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    

    # Busqueda de producto por modelo

    def consultar_producto_codigo(self, modelo):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (modelo,))
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color= row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False
    
    # Busqueda de producto por color

    def consultar_producto_codigo(self, color):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (color,))
        row = self.cursor.fetchone()
        if row:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color= row
            return Auto(codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color)
        return False

    

    def modificar_producto(self,codigo, nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color)
            self.cursor.execute("UPDATE productos SET descripcion = ?, cantidad = ?, precio = ? WHERE codigo = ?",
                                (nuevo_cantidad, nuevo_marca, nuevo_modelo, nuevo_motor, nuevo_potencia, nuevo_velocidad, nuevo_peso, nuevo_color, codigo))
            self.conexion.commit()


    def listar_productos(self):
        print("-" * 30)
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, cantidad, marca, modelo, motor, potencia, velocidad, peso, color = row
            print(f"Código: {codigo}")
            print(f"Marca: {marca}")
            print(f"Modelo: {modelo}")
            print(f"Cantidad: {cantidad}")
            print(f"Motor: {motor}")
            print(f"Potencia: {potencia}")
            print(f"Velocidad: {velocidad}")
            print(f"Peso : {peso}")
            print(f"Color: {color}")
            print("-" * 30)

    def eliminar_producto(self, codigo):
        self.cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            print("Producto eliminado.")
            self.conexion.commit()
        else:
            print("Producto no encontrado.")
    



    