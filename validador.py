"""
Validador de ficheros XML Y XSD

"""
import sys
from xmlschema import XMLSchema
from flask import Flask
import xml.etree.ElementTree as ET
import xmltodict
import json


app = Flask(__name__)

def validador(xml_file, xsd_file, xpath, json_var):
    """Recogemos XML y lo validamos"""
    """En la parte dos, tenemos que pasarle un elemento del xml y ser capaces de leer el valor de dicho elemento, el parámetro IMPORT es XPATH"""

    tree = ET.parse(xml_file)
    root = tree.getroot()
    print(root)
    try:
        esquemaXML = XMLSchema(xsd_file)
        esquemaXML.validate(xml_file)
        print(f"{xml_file} ok según {xsd_file}.")
    except Exception as error:
        print("upps something went wrong")
        sys.exit(1)


    if xpath:
        print(f"ok, es el {xpath}")

        elementos = xpath.split("/")

        elementos = [elemento for elemento in elementos if elemento]

        elemento_principal = elementos[0] if len(elementos) > 0 else None
        atributo = elementos[-1] if len(elementos) > 1 else None


        for elem in root.iter(elemento_principal):
            print(elem.tag)
            for child in elem:
                if(child.tag == atributo):
                    print(child.tag)
                    """Devuelve Veronica"""
                    print(child.text)
                    
    else:
        print('not ok')

    if json_var == True:
        with open('carta.xml', 'r') as xml_file:
            xml_content = xml_file.read()
            print(xml_content)
        xml_python = xmltodict.parse(xml_content)
        json_data = json.dumps(xml_python, indent=4)

        with open('carta.json', 'w') as json_file:
            json_file.write(json_data)
        print("JSON Generado")
    else:
        print("no se genera fichero")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python validador.py carta.xml carta.xsd")
        sys.exit(1)

    archivo_xml = sys.argv[1]
    """valor que le pasamos a la función como p1, lo sacamos de ejecuta desde la consola el comando: python validador.py carta.xml carta.xsd"""
    print(archivo_xml)
    archivo_xsd = sys.argv[2]
    """valor que le pasamos a la función como p2, lo sacamos de ejecuta desde la consola el comando: python validador.py carta.xml carta.xsd"""
    print(archivo_xsd) 
    xpath = "/remitente//nombre"
    json_var = True

validador(archivo_xml, archivo_xsd, xpath, json_var)

