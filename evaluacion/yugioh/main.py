from fastapi import FastAPI, Query
import csv
from pydantic import BaseModel
import qrcode

app = FastAPI()

class Yugioh(BaseModel):
    id_carta: int
    nombre: str
    tipo: str
    atributo: str
    nivel: str
    atk: str
    defe: str
    efecto: str
    tipo_carta: str  # Nuevo campo para el tipo de carta (Fusión, Sincronía, etc.)

@app.get("/", status_code=200,
    summary="Endpoint raiz",
    description="Endpoint raíz de la API")
def get_cartas_m():
    response = []

    # Abre el archivo "yugi.csv" y agrega sus datos
    with open("yugi.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")

        for fila in reader:
            response.append(fila)

    # Abre el archivo "magias_trampas.csv" y agrega sus datos
    with open("magias_trampas.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=",")

        for fila in reader:
            response.append(fila)

    return response


@app.get("/v1/monstruo", response_model=list[Yugioh],
    summary="Endpoint para visualizar datos",
    description="Endpoint para visualizar datos de la API")
async def get_cartas_m1(nombre: str = Query(...)):
    response = []

    with open("yugi.csv", "r") as file1:
        reader1 = csv.DictReader(file1, delimiter=",")

        for fila in reader1:
            if fila.get("nombre") == nombre:
                response.append(fila)

    return response

@app.get("/v1/monstruo/{id_carta}",
    summary="Endpoint para visualizar datos de un contacto",
    description="Endpoint para visualizar datos de un contacto de la API")
async def get_cartas_m(id_carta: int):
    with open("yugi.csv", "r") as file1:
        reader1 = csv.DictReader(file1, delimiter=",")

        for fila in reader1:
            if fila.get("id_carta") == str(id_carta):
                return fila

    raise {"Error": "Carta no encontrada"}

@app.post("/v1/monstruo", status_code=201,
    summary="Endpoint para enviar datos",
    description="Endpoint para enviar datos a la API")
def post_carta(carta: Yugioh):
    with open("yugi.csv", "a", newline="") as file:
        fieldnames = ["id_carta", "nombre", "tipo", "atributo", "nivel", "atk", "defe", "efecto", "tipo_carta"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow({
            "id_carta": carta.id_carta,
            "nombre": carta.nombre,
            "tipo": carta.tipo,
            "atributo": carta.atributo,
            "nivel": carta.nivel,
            "atk": carta.atk,
            "defe": carta.defe,
            "efecto": carta.efecto,
            "tipo_carta": carta.tipo_carta
        })

    return {"mensaje": "Datos de la carta agregados con éxito"}

@app.put("/v1/monstruo/{id_carta}", status_code=200,
    summary="Endpoint para actualizar datos",
    description="Endpoint para actualizar datos de un contacto en la API")
def put_carta(id_carta: int, carta: Yugioh):
    cartas = []

    with open("yugi.csv", "r") as file:
        cartas = list(csv.DictReader(file))

    updated = False
    for fila in cartas:
        if fila.get("id_carta") == str(id_carta):
            fila["nombre"] = carta.nombre
            fila["tipo"] = carta.tipo
            fila["atributo"] = carta.atributo
            fila["nivel"] = carta.nivel
            fila["atk"] = carta.atk
            fila["defe"] = carta.defe
            fila["efecto"] = carta.efecto
            fila["tipo_carta"] = carta.tipo_carta
            updated = True

    if not updated:
        raise {"Error": "Carta no encontrada"}

    with open("yugi.csv", "w", newline="") as file:
        fieldnames = ["id_carta", "nombre", "tipo", "atributo", "nivel", "atk", "defe", "efecto", "tipo_carta"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cartas)

    return {"mensaje": "Datos de la carta actualizados con éxito"}

@app.delete("/v1/monstruo/{id_carta}", status_code=204,
    summary="Endpoint para borrar datos",
    description="Endpoint para borrar datos de la API")
def delete_carta(id_carta: int):
    cartas = []

    with open("yugi.csv", 'r') as file:
        reader = csv.DictReader(file, delimiter=",")
        fieldnames = ["id_carta", "nombre", "tipo", "atributo", "nivel", "atk", "defe", "efecto", "tipo_carta"]

        for fila in reader:
            if int(fila.get("id_carta")) != id_carta:
                cartas.append(fila)

    with open("yugi.csv", 'w', newline='') as salida:
        writer = csv.DictWriter(salida, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cartas)

    return None


class Magia_trampa(BaseModel):
    id_carta: int
    nombre: str
    tipo: str
    efecto: str
    tipo_carta: str  # Nuevo campo para el tipo de carta (Fusión, Sincronía, etc.)

@app.get("/v1/magia_trampas/{id_carta}",
    summary="Endpoint para visualizar datos de un contacto",
    description="Endpoint para visualizar datos de un contacto de la API")
async def get_cartas_m(id_carta: int):
    with open("magias_trampas.csv", "r") as file1:
        reader1 = csv.DictReader(file1, delimiter=",")

        for fila in reader1:
            if fila.get("id_carta") == str(id_carta):
                return fila

    raise {"Error": "Carta no encontrada"}

@app.post("/v1/magia_trampas", status_code=201,
    summary="Endpoint para enviar datos",
    description="Endpoint para enviar datos a la API")
def post_carta(carta: Magia_trampa):
    with open("magias_trampas.csv", "a", newline="") as file:
        fieldnames = ["id_carta", "nombre", "tipo", "efecto", "tipo_carta"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writerow({
            "id_carta": carta.id_carta,
            "nombre": carta.nombre,
            "tipo": carta.tipo,
            "efecto": carta.efecto,
            "tipo_carta": carta.tipo_carta
        })

    return {"mensaje": "Datos de la carta agregados con éxito"}

@app.put("/v1/magia_trampas/{id_carta}", status_code=200,
    summary="Endpoint para actualizar datos",
    description="Endpoint para actualizar datos de un contacto en la API")
def put_carta(id_carta: int, carta: Magia_trampa):
    cartas = []

    with open("magias_trampas.csv", "r") as file:
        cartas = list(csv.DictReader(file))

    updated = False
    for fila in cartas:
        if fila.get("id_carta") == str(id_carta):
            fila["nombre"] = carta.nombre
            fila["tipo"] = carta.tipo
            fila["efecto"] = carta.efecto
            fila["tipo_carta"] = carta.tipo_carta
            updated = True

    if not updated:
        raise {"Error": "Carta no encontrada"}

    with open("magias_trampas.csv", "w", newline="") as file:
        fieldnames = ["id_carta", "nombre", "tipo", "efecto", "tipo_carta"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cartas)

    return {"mensaje": "Datos de la carta actualizados con éxito"}

@app.delete("/v1/magia_trampas/{id_carta}", status_code=204,
    summary="Endpoint para borrar datos",
    description="Endpoint para borrar datos de la API")
def delete_carta(id_carta: int):
    cartas = []

    with open("magias_trampas.csv", 'r') as file:
        reader = csv.DictReader(file, delimiter=",")
        fieldnames = ["id_carta", "nombre", "tipo", "efecto", "tipo_carta"]

        for fila in reader:
            if int(fila.get("id_carta")) != id_carta:
                cartas.append(fila)

    with open("magias_trampas.csv", 'w', newline='') as salida:
        writer = csv.DictWriter(salida, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cartas)

    return None
 
API_BASE_URL = "https://8000-osaradahir-api-l99jx8le0ud.ws-us105.gitpod.io/"  # Reemplaza con la URL de tu API

# Define la función para generar un código QR
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Ruta para generar un código QR
@app.get("/generar_qr")
def generate_qr():
    # Genera un nombre de archivo único para cada código QR
    qr_filename = "api_yugioh.png"
    # Genera el código QR con la URL de la API
    generate_qr_code(API_BASE_URL, qr_filename)
    return {"message": "Código QR generado con éxito"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)