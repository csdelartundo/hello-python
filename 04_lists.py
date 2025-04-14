###Lists###
# Ordenada.
# Mutable (puedes modificar elementos).
# Permite duplicados.

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(type(my_list))
print(my_list)
print(len(my_list))

my_other_list = [29, 1.59, "Constanza", "Salinas"]
print(type(my_other_list))
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
# print(my_other_list[-5]) error
# print(my_other_list[4]) error
print(len(my_other_list))
print(my_other_list.count("Constanza"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

# my_other_list_obj = [{"hola", "que", "tal", 11}] toma un objeto como un elemento de la lista
# print(type(my_other_list_obj))
# print(my_other_list_obj)
# print(len(my_other_list_obj))
# print(my_other_list_obj[0])

my_list = "Hola Python"
print(my_list)

my_other_list.append("Whitezoe")
print(my_other_list)
my_other_list.insert(1, "Rojo")
print(my_other_list)
my_other_list.remove("Rojo")
print(my_other_list)
my_other_list.pop()
print(my_other_list)

my_pop_element = my_other_list.pop(2) #elimina el elemento y tb lo devuelve
print(my_pop_element)
print(my_other_list)

del my_other_list[2] #elimina por indice
print(my_other_list)

my_new_list = my_other_list.copy() #copia la lista
my_other_list.clear()
print(my_other_list)
print(my_new_list) #no se borra la lista original

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() #ordena ascendente por defecto
print(my_new_list)