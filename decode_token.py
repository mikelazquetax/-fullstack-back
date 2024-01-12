"""
Decoficador de Tokens

"""

import jwt
import argparse

def decode_jwt(token, secret):
    try:
        # Decodificar el token JWT utilizando HS256
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        print("Error: Token expirado.")
    except jwt.InvalidTokenError:
        print("Error: Token no válido (puede deberse a una firma incorrecta).")
    except Exception as e:
        print(f"Error: {str(e)}")
    return None

def main():
    # Configurar el parser de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Decodificador de tokens JWT')
    parser.add_argument('--token', required=True, help='Token JWT a decodificar')
    parser.add_argument('--secret', required=True, help='Secreto de la firma del token')
    parser.add_argument('--field', help='Nombre de un campo dentro del cuerpo del token JWT')

    # Obtener los argumentos del comando
    args = parser.parse_args()

    # Decodificar el token
    decoded_token = decode_jwt(args.token, args.secret)

    if decoded_token:
        # Verificar si se solicita un campo específico
        print(args)
        if args.field:
            field_value = decoded_token.get(args.field, "No encontrado")
            print(f"{args.field}: {field_value}")
        else:
            print("Contenido completo del cuerpo del token:")
            print(decoded_token)



if __name__ == "__main__":
    main()