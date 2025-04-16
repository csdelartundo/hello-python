###Bucles/Loops/Ciclos###

#While

my_condition = 0

while my_condition < 10: #podria considerarse como un if que se repite
    print(my_condition)
    my_condition += 2 #incrementa de 2 en 2
else: #es opcional
    print("Mi condicion es mayor o igual que 10")

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print("Mi condicion es igual a 16")
        break #rompe el bucle
    print(my_condition)

#For
#Recorre los elementos, e imprime las claves, no valores

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #recorre la lista
    print(element)

my_tuple = (35, 1.77, "Constanza", "Salinas", "Constanza")
for element in my_tuple:
    print(element)

my_set = {"Constanza", "Salinas", 29}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Constanza", "Apellido":"Salinas", "Edad":29, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Apellido":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("Se ejecuta")

my_dict = {"Nombre":"Constanza", "Apellido":"Salinas", "Edad":29, 1:"Python"}
for element in my_dict:
    print(element)
    if element == "Apellido":
        continue
else:
    print("El bucle for para diccionario ha finalizado")