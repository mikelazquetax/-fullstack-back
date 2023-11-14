""" Pruebas de Calculadora """
import time
import calculadora


def test_sumar():
    """ Prueba Funcion Sumar """
    time.sleep(1)
    a = 2
    b = 2
    c = calculadora.sumar(a, b)
    assert c == 4

def test_restar():
    """ Prueba Funcion restar """ 
    time.sleep(1)
    a = 2
    b = 2
    c = calculadora.restar(a, b)
    assert c == 0
