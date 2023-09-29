@app.post("/v1/contactos")
def post_contactos(
    id_contacto: str,
    nombre: str,
    primer_apellido: str,
    segundo_apellido: str,
    email: str,
    telefono: str
):
    # Escribir los datos en el archivo "contactos.csv"
    with open("contactos.csv", "a", newline="") as file:
        fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()

        # Escribir los datos del nuevo contacto
        writer.writerow({
            "id_contacto": id_contacto,
            "nombre": nombre,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "email": email,
            "telefono": telefono
        })

    return {"mensaje": "Datos de contacto agregados con éxito"}
