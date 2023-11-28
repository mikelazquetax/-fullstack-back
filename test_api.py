""" 
Pruebas de api 
"""
import pytest
import api


def test_obtener_primer_elemento():
    """ Prueba Obtener primer elemento """
    lista = ["master", "full", "stack"]
    elemento = api.obtener_primer_elemento(lista)
    assert elemento == "master"

def test_inserta_elemento_al_final():
    """ Prueba Insertar elemento al final """
    lista = ["master", "full", "stack"]
    api.inserta_elemento_al_final(lista, "hola")
    assert lista == ["master","full","stack","hola"]

def test_inserta_elemento_al_principio():
    """ Prueba Insertar elemento al principio """
    lista = ["master", "full", "stack"]
    api.inserta_elemento_al_principio(lista, "hola")
    assert lista == ["hola", "master", "full", "stack"]

def test_borra_lista():
    """ Prueba borrar lista """
    lista = ["master", "full", "stack"]
    api.borra_lista(lista)
    assert not lista

if __name__ == "__main__":
    pytest.main()
