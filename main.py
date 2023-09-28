from typing import Union

from fastapi import FastAPI
import csv
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/contactos")
def get_contactos():
    response = []

    with open("contactos.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")

        for fila in reader:
            response.append(fila)

    return response
