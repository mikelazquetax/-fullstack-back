"""OPERACIONES CRUD"""
import sys


def llamada_api(method, resource, resource_id=''):
    print(method,resource,resource_id)
if __name__ == "__main__":
    """Ejecutar este comando en consola:  py main.py --method POST --resource posts --resource_id 1"""
    if len(sys.argv) != 5 and sys.argv[2] == 'GET':
        print("Malformación: resource_id solo necesario en métodos POST,PUT Y DELETE")
        sys.exit(1)
    else:
        print("método empleado: " + sys.argv[2])
        print(len(sys.argv))
        
        method = sys.argv[2]
        
        resource = sys.argv[4]
        
    if len(sys.argv) > 5:
        resource_id = sys.argv[6]
    else:
        resource_id = ''
llamada_api(method, resource, resource_id)


