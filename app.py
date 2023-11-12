from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

def prepara():
    return render_template('prepara_pedido.html')

@app.route("/pizza", methods=['POST'])
def pizza():
    nombreCliente = request.form.get("p1")
    apellidoCliente = request.form.get("p2")
    print(nombreCliente)
    print(apellidoCliente)
    guardar_pedido(nombreCliente, apellidoCliente)
    return redirect(url_for('solicita_pedido', nombreCliente=nombreCliente, apellidoCliente=apellidoCliente))

def guardar_pedido(nombreCliente, apellidoCliente):
    with open("pedidosPizza.txt", "a", encoding="utf-8") as file:
        file.write(nombreCliente + " " + apellidoCliente + "\n")
        file.close()  

@app.route('/solicita_pedido')
def solicita_pedido():
    # Obtener valores de la URL
    nombreCliente = request.args.get('nombreCliente')
    apellidoCliente = request.args.get('apellidoCliente')

    # Renderizar la plantilla de resultados con los valores
    return render_template('solicita_pedido.html', nombreCliente=nombreCliente, apellidoCliente=apellidoCliente)

if __name__ == '__main__':
    app.run(debug=True)
