"""
Generador de Tokens

"""

import json
import uuid
import jwt
import argparse


def token_generation(payload, secret):

    with open(payload, 'r') as file:
        payload_data = json.load(file)
        print(payload_data)
    
    jti = str(uuid.uuid4())
    payload_data['jti'] = jti
    token = jwt.encode(payload_data, secret, algorithm='HS256')

    return token


def token_en_json(payload_file, token):
    """leemos el fichero payload.json"""
    with open(payload_file, 'r') as file:
        payload_data = json.load(file)

    """Le metemos el parámetro JWT ID al objeto"""
    payload_data['JWT ID'] = token

    """Actualizamos el fichero payload.json con el nuevo valor token"""
    with open(payload_file, 'w') as file:
        json.dump(payload_data, file, indent=4)


def main():

    parser = argparse.ArgumentParser(description='Generador de tokens JWT')
    parser.add_argument('--payload', required=True, help='payload.json')
    parser.add_argument('--secret', required=True, help='XXXXYYYY')
    
    args = parser.parse_args()

    token = token_generation(args.payload, args.secret)

    print(token)

    token_en_json(args.payload, token)

    
    with open(args.payload, 'r') as file:
        updated_payload_data = json.load(file)
        print("Contenido actualizado del archivo payload.json:")
        """Una vez actualizado el JSON lo imprimimos por consola"""
        print(json.dumps(updated_payload_data, indent=4))

if __name__ == "__main__":
    """Ejecutar este comando en consola: python code_token.py --payload payload.json --secret XXXXYYYY"""
    main()
