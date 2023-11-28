"""
Pruebas Persistencia
"""
import persistencia
def test_guardar_pedido():
 """
 Prueba general
 """
 with open("pedidos.txt", "w+", encoding="utf-8") as file:
persistencia.guardar_pedido("Pedro", "Gil de Diego")
persistencia.guardar_pedido("Michael", "Jordan")
firstline = file.readline()
secondline = file.readline()
file.close()
 assert firstline == "-Pedro Gil de Diego\n"
 assert secondline == "-Michael Jordan\n"