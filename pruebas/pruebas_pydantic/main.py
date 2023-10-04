from fastapi import FastAPI
import csv
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/", status_code=200,
    summary="Endpoint raiz",
    description="Endpoint raiz de la API")
 
def get_contactos():
    response = []

    with open("contactos.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")

        for fila in reader:
            response.append(fila)

    return response

@app.get("/v1/contactos", status_code=298,
    summary="Endpoint para visualizar datos",
    description="Endpoint para visualizar datos de la API")

def get_contactos1():
    response = []

    with open("contactos_n.csv", "r") as file1:
        reader1 = csv.DictReader(file1, delimiter=",")

        for fila in reader1:
            response.append(fila)
            
    return response

class Contactos(BaseModel):
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: int

@app.post("/v1/contactos", status_code=201,
    summary="Endpoint para enviar datos",
    description="Endpoint para enviar datos a la API")
def post_contactos(contacto: Contactos):

    with open("contactos_n.csv", "a", newline="") as file:
        fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writerow({
            "id_contacto": contacto.id_contacto,
            "nombre": contacto.nombre,
            "primer_apellido": contacto.primer_apellido,
            "segundo_apellido": contacto.segundo_apellido,
            "email": contacto.email,
            "telefono": contacto.telefono
        })

    return {"mensaje": "Datos de contacto agregados con éxito"}

