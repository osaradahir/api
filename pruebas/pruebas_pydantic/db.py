import requests 
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

# print(f"GET :  {response.text}")

response_json = json.loads(response.text)

print(f"1.-{response_json['results'] [0] ['name']}")
print(f"2.-{response_json['results'] [1] ['name']}")
print(f"3.-{response_json['results'] [2] ['name']}")
print(f"4.-{response_json['results'] [3] ['name']}")
print(f"5.-{response_json['results'] [4] ['name']}")
print(f"6.-{response_json['results'] [5] ['name']}")
print(f"7.-{response_json['results'] [6] ['name']}")
print(f"8.-{response_json['results'] [7] ['name']}")
print(f"9.-{response_json['results'] [8] ['name']}")
print(f"10.-{response_json['results'] [9] ['name']}")
print(f"11.-{response_json['results'] [10] ['name']}")
print(f"12.-{response_json['results'] [11] ['name']}")

print("¿Quieres ver sus capacidades?")
num = int(input("Selcciona un personaje: "))

if 1 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/barbarian']
    for i, proficiency in enumerate(proficiencies[:12], start=1):
        print(f"{i}. {proficiency['name']}")
elif 2 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/bard']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 3 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/cleric']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 4 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/druid']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 5 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/fighter']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 6 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/monk']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 7 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/paladin']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 8 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/ranger']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 9 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/rogue']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 10 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/sorcerer']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 11 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/warlock']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
elif 12 == num:
    class_1= ['https://www.dnd5eapi.co/api/classes/wizard']
    for i, proficiency in enumerate(proficiencies[:8], start=1):
        print(f"{i}. {proficiency['name']}")
else:
    print("Opcion no valida")





