"""
Validador de ficheros XML Y XSD

"""
import sys
from xmlschema import XMLSchema
from flask import Flask
import xml.etree.ElementTree as ET


app = Flask(__name__)

def validador(xml_file, xsd_file, xpath):
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
        for elem in root.iter(xpath):
            print(elem.tag)
            for child in elem:
                print(child.tag)
                if (child.text and child.tag == "nombre"):
                    """Devuelve Veronica"""
                    return child.text
    else:
        print('not ok')

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
    xpath = "remitente"

valor = validador(archivo_xml, archivo_xsd, xpath)
print(valor)
