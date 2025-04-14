###Diccionarios###
#Almacena pares clave:valor

my_dict = {}
my_other_dict = dict()
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Constanza", "Apellido":"Salinas", "Edad":29, 1:"Python"}#relacion clave:valor
print(len(my_other_dict))

my_dict = {
    "Nombre":"Constanza",
    "Apellido":"Salinas",
    "Edad":29,
    "Lenguajes":{
        "Python", 
        "Swift", 
        "Kotlin"
        },
    1:1.59
    }

print(my_dict)
print(len(my_dict))

my_dict["Nombre"] = "Whitezoe"
print(my_dict["Nombre"])#permite acceder a un elemento

print(my_dict[1])

my_dict["Calle"] = "Las Flores" #agrega un nuevo elemento
print(my_dict)

my_dict.pop(1) #elimina un elemento
print(my_dict)
print("Constanza" in my_dict)#busca el elemento
print("Apellido" in my_dict)
print(my_dict.items())#muestra los elementos como uno solo, en un listado
print(my_dict.keys())#elemento clave
print(my_dict.values())#el valor
print(my_dict.fromkeys(("Nombre", 1)))#crea un diccionario nuevo sin valores (crea la clave)

my_dict.update({"Lenguajes":"Python"})#actualiza el diccionario
print(my_dict)

# my_new_dict = dict.fromkeys("Nombre", "Calle")#crea un diccionario nuevo sin valores
# print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Cota")#le di el mismo valor a todas las claves
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))