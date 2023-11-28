"""
Creacion de Pedidos
"""
from flask import Flask, request, redirect, render_template, url_for, Response

app = Flask(__name__)

def prepara():
    """Renderizacion de pantalla"""
    return render_template('prepara_pedido.html')

@app.route("/pizza", methods=['POST'])
def pizza():
    """Crea la solicitud de pizza y redirige a la pantalla final"""
    nombre_cliente = request.form.get("p1")
    apellido_cliente = request.form.get("p2")
    print(nombre_cliente)
    print(apellido_cliente)
    guardar_pedido(nombre_cliente, apellido_cliente)
    return redirect(url_for('solicita_pedido',
    nombreCliente=nombre_cliente,apellidoCliente=apellido_cliente))

def guardar_pedido(nombre_cliente, apellido_cliente):
    """Guarda el nombre del cliente en el archivo pedidosPizza.txt"""
    with open("pedidosPizza.txt", "a", encoding="utf-8") as file:
        file.write(nombre_cliente + " " + apellido_cliente + "\n")
        file.close()

@app.route("/checksize", methods=['POST'])
def checksize():
    """Obtiene el tamaño de la pizza y devuelve su disponibilidad en Pantalla"""
    pizza_size = request.args.get('p6')
    print(pizza_size)
    if pizza_size == 'S':
        mensaje = 'No Disponible'
    else:
        mensaje = 'Disponible'
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

@app.route('/solicita_pedido')
def solicita_pedido():
    """Mostrar pagina final"""
    # Obtener valores de la URL
    nombre_cliente = request.args.get('nombreCliente')
    apellido_cliente = request.args.get('apellidoCliente')

    # Renderizar la plantilla de resultados con los valores
    return render_template('solicita_pedido.html',
    nombreCliente=nombre_cliente,apellidoCliente=apellido_cliente)

if __name__ == '__main__':
    app.run(debug=True)
