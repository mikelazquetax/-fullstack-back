import sqlite3 as sql
import requests
import sys
import argparse

def createDBAlmacen():
    conn = sql.connect("almacen.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE WAREHOUSE (
            idWarehouse integer,
            idProduct integer,
            productName text,
            productCount integer,
            productAvailable bool
        )"""
    )
    conn.commit()
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Realiza operaciones CRUD en una API de almacenes')
    parser.add_argument('--servidor', default='localhost', required=False, help='Método de la operación CRUD')
    parser.add_argument('--puerto', required=False, default='5000' help='Recurso de la API')
    parser.add_argument('--config', required=True, default='', help='Ruta y Nombre del fichero de configuracion')

    conexion_api(args.servidor,args.puerto,args.config)

if __name__ == "__main__":
    print("hola")
    main()
    createDBAlmacen()
    createTable()