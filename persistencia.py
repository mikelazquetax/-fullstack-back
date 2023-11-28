"""Def funcion para guardar fichero pedidos.txt"""
def guardar_pedido(nombre, apellidos):
    """Abrir, escribir y cerrar"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
