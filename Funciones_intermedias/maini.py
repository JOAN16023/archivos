#Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes_4b = [
    {"first_name": "benja", "last_name": "jordan"},
    {"first_name": "papitas", "last_name": "matias"},
]
de_deportes = {
    "basketball": ["maxi", "vicente", "joan", "daniel"],
    "futbol": ["Messi", "cristiano_Ronaldo", "Jude Bellingham"],
}
z = [{"x": 10, "y": 20}]
x[1][0] = 15
estudiantes_4b[0]["last_name"] = "bryant"

de_deportes["futbol"][0] = "andres"
z[0]["y"] = 30

#Iterar a través de una lista de diccionarios

def interactuar(lista):
    for elementos in lista:
        output = ""
        for key, value in elementos.items():
            output += f"{key} - {value}, "
        print(output[:-2])
interactuar(estudiantes_4b)


#Obtener valores de una lista de diccionarios

def inecta(nombre, lista1):
    for item in lista1:
        print(item[nombre])
inecta("first_name", estudiantes_4b)
inecta("last_name", estudiantes_4b)


#Iterar a través de un diccionarios con valores de lista

def muestra(muestra2):
    for key, value in muestra2.items():
        print(f"{len(value)} {key.upper()}")
        for evalua in value:
            print(evalua)

print("---------------")
coding_dojo = {
    "Ubicaciones": [
        "San ramon",
        "Cisterna",
        "Pintana",
        "Granja",
        "Florida",
        "Estacion central",
        "Las condes",
    ],
    "Instructores": [
        "tonio",
        "felipe",
        "tomas",
        "roberto",
        "moongral",
        "Mrsavage",
        "bugha",
        "tfue",
    ],
}
muestra(coding_dojo)
