"""Run test"""
def obtener_primer_elemento(lista):
    """Obtener Primer elemento de la lista"""
    return lista[0]


def inserta_elemento_al_final(lista, elemento):
    """Insertar elemento al final"""
    lista.append(elemento)


def inserta_elemento_al_principio(lista, elemento):
    """Insertar elemento al principio"""
    lista.insert(0, elemento)


def borra_lista(lista):
    """Eliminar lista"""
    lista.clear()
