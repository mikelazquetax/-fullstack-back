import argparse
import sqlite3 as sql
import yaml
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

# Argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Aplicación de Almacén')
parser.add_argument('--servidor', default='localhost', help='IP o nombre del servidor (por defecto: localhost)')
parser.add_argument('--puerto', type=int, default=5000, help='Puerto para exponer el API (por defecto: 5000)')
parser.add_argument('--config', required=True, help='Ruta y nombre del fichero de configuración YAML')
args = parser.parse_args()

# Cargar la configuración desde el archivo YAML
with open(args.config, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Crear conexión a la base de datos SQLite
conn = sql.connect(config['basedatos']['path'])
c = conn.cursor()

api_key = config['basedatos']['consumidor_almacen_key']

# Crear tabla si no existe
c.execute('''CREATE TABLE IF NOT EXISTS productos (
            idProduct integer PRIMARY KEY AUTOINCREMENT,
            productName text,
            productCount integer, 
            productAvailable BOOLEAN
             )''')
conn.commit()

#Insertamos un unico producto para tener datos
def insertProduct(idProduct, productName, productCount, productAvailable):
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()
    instruccion = f"INSERT INTO productos values ({idProduct},'{productName}',{productCount},{productAvailable})"
    c.execute(instruccion)
    conn.commit()
    conn.close()


# Ruta para obtener la lista de productos
@app.route('/warehouse/productos', methods=['GET'])
def obtener_productos():
    try:
        conn = sql.connect(config['basedatos']['path'])
        c = conn.cursor()
        c.execute('SELECT * FROM productos')
        productos = [{'idProduct': row[0], 'productName': row[1], 'productCount': row[2], 'productAvailable': row[3]} for row in c.fetchall()]
        conn.close()
        return jsonify(productos)
        print(productos)
    except sql.Error as e:
        return jsonify({'error': str(e)}), 500
        

# Ruta para obtener detalles de un producto específico
@app.route('/warehouse/productos/<int:idProduct>', methods=['GET'])
def obtener_detalle_producto(idProduct):
    print(idProduct)
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()
    c.execute("SELECT * FROM productos WHERE idProduct = ?", (idProduct,))
    producto = c.fetchone()
    print(producto)
    conn.close()
    if producto:
        return jsonify({'idProduct': producto[0], 'productName': producto[1], 'productCount': producto[2], 'productAvailable': producto[3]})
    else:
        return jsonify({'mensaje': 'Producto no encontrado'}), 404

# Ruta para actualizar datos de Producto
@app.route('/warehouse/productos/<int:idProduct>', methods=['PUT'])
def actualizar_producto(idProduct):
    data = request.json
    productAvailable = data.get('productAvailable')
    productCount = data.get('productCount')
    productName = data.get('productName')
    print(idProduct)
    print(data)
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()

    c.execute('UPDATE productos SET productAvailable = ? WHERE idProduct = ?', (productAvailable, idProduct))
    c.execute('UPDATE productos SET productCount = ? WHERE idProduct = ?', (productCount, idProduct))
    c.execute('UPDATE productos SET productName = ? WHERE idProduct = ?', (productName, idProduct))
    conn.commit()
    return jsonify({'mensaje': 'Product updated successfully'})

# Ruta para crear datos de Producto
@app.route('/warehouse/productos/<int:idProduct>', methods=['POST'])
def crear_producto_nuevo(idProduct):
    data = request.json
    print(idProduct)
    print(data)
    productAvailable = data.get('productAvailable')
    productCount = data.get('productCount')
    productName = data.get('productName')
    
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()

    instruccion = f"INSERT INTO productos values ({idProduct},'{productName}',{productCount},{productAvailable})"
    c.execute(instruccion)

    conn.commit()
    return jsonify({'mensaje': 'Product Created Successfully'})

@app.route('/warehouse/productos/<int:idProduct>', methods=['DELETE'])
def delete_producto(idProduct):
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()
    c.execute('DELETE FROM productos WHERE idProduct = ?', (idProduct,))
    conn.commit()
    return jsonify({'mensaje': 'Product Deleted Successfully'})   

# Ruta para actualizar datos de Producto  python almacen.py --config config.yaml
@app.route('/warehouse/productQuantity/<int:idProduct>', methods=['PUT'])
def actualizar_producto_quantity(idProduct):
    data = request.json
    operation = data.get('operation')
    print(operation)
    conn = sql.connect(config['basedatos']['path'])
    c = conn.cursor()
   
    c.execute("SELECT * FROM productos WHERE idProduct = ?", (idProduct,))
    producto = c.fetchone()
    print(producto)
    quantity = producto[2]

    if operation == 'decrease':
        quantity = quantity - 1
    elif operation == 'increase':
        quantity = quantity + 1
    else:
        return

    c.execute('UPDATE productos SET productCount = ? WHERE idProduct = ?', (quantity, idProduct))
  
    conn.commit()
    return jsonify({'mensaje': 'Product updated successfully'})

if __name__ == '__main__':
    app.run(host=args.servidor, port=args.puerto)
    insertProduct(1,'Apples', 125, 0)