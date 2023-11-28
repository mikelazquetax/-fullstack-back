def obtener_primer_elemento(lista):
    return lista[0]

def inserta_elemento_al_final(lista, elemento):
    lista.append(elemento)

def inserta_elemento_al_principio(lista, elemento):
    lista.insert(0, elemento)

def borra_lista(lista):
    lista.clear()