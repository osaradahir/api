import requests 

URI = "http://localhost:8000/v1/contactos"

response = requests.get(URI)

print(f"GET :  {response.text}")
print(f"GET :  {response.status_code}")

data = {
  "id_contacto": 16,
  "nombre": "oscar",
  "primer_apellido": "nose",
  "segundo_apellido": "nose",
  "email": "prueba@email.com",
  "telefono": 11214
}

response = requests.post(URI, json=data)

print(f"POST : {response.text}")
print(f"POST :  {response.status_code}")

response = requests.put(URI)
