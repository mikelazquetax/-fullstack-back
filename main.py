"""OPERACIONES CRUD"""
import sys
import argparse
import requests
import json

def leer_configuracion():
    try:
        with open('config.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Error: No se encontró el archivo config.json')
        return None
    except json.JSONDecodeError as e:
        print(f'Error al decodificar el archivo JSON config.json: {e}')
        return None

def leer_json(resource):

    try:
        with open(f'{resource}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: No se encontró el archivo {resource}.json')
        return None
    except json.JSONDecodeError as e:
        print(f'Error al decodificar el archivo JSON {resource}.json: {e}')
        return None

def guardar_datos_en_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(f'Error al guardar datos en el archivo {filename}: {e}')

def adaptar_a_json_api(data):
    return data

def llamada_api(method, resource, resource_id,url, request_timeout, response_data_filename, response_status_filename):
    print(method,resource,resource_id)

    
    if method == 'GET' and not resource_id:
        url = f'https://jsonplaceholder.typicode.com/{resource}'
        response = requests.get(url)
        print(response.json()) 
    elif method == 'GET' and resource_id:
        url = f'https://jsonplaceholder.typicode.com/{resource}/{resource_id}'
        response = requests.get(url)
        print(response.json()) 
    """imprimimos respuesta de la llamada GET"""

    if method in ['POST', 'PUT']:
        """Funcion que abre el json en concreto y, devuelve en el data los valores del json"""
        data = leer_json(resource) 
        if data is None:
            return
        else:
            print(data)

    if method == 'POST':
        url = f'https://jsonplaceholder.typicode.com/{resource}/{resource_id}'
        response = requests.post(url, json=data)
    elif method == 'PUT':
        url = f'https://jsonplaceholder.typicode.com/{resource}/{resource_id}'
        response = requests.put(url, json=data)

    print(response.json())
    print(response)

    response_info = {
        'Method': method,
        'Url': response.url,
        'Status': response.status_code,
        'Content-type': response.headers.get('content-type'),
        'Encoding': response.encoding
    }

    response_json_adaptado = adaptar_a_json_api(response.json())

    guardar_datos_en_json(response_info, response_status_filename)

    guardar_datos_en_json(response.json(), response_data_filename)

    print(response_json_adaptado)

def main():
    parser = argparse.ArgumentParser(description='Realiza operaciones CRUD en una API')
    parser.add_argument('--method', choices=['GET', 'POST', 'PUT', 'DELETE'], required=True, help='Método de la operación CRUD')
    parser.add_argument('--resource', required=True, help='Recurso de la API')
    parser.add_argument('--resource_id', default='', help='Identificador único del recurso para operaciones específicas')

    args = parser.parse_args()

    config = leer_configuracion()
    if config is None:
        return
    

    llamada_api(args.method, args.resource, args.resource_id, config['url'], config['request_time_out'], config['response_data'], config['response_status'])

if __name__ == "__main__":
    main()


