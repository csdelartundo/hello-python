###Sets###

# No ordenado.
# Mutable (pero no permite elementos mutables dentro).
# No permite duplicados.

my_set = set() #tipo de dato
print(type(my_set))

my_other_set = {}
print(type(my_other_set)) #inicialmente es un diccionario
my_other_set = {"Constanza", "Salinas", 29}
print(type(my_other_set))

len(my_other_set)
print(len(my_other_set))

my_other_set.add("Whitezoe")
print(my_other_set) #un set no es una estructura ordenada

my_other_set.add("Whitedalu")
print(my_other_set) #un set no es una estructura ordenada

print("Constanza" in my_other_set)
print("constanza" in my_other_set) #distintas mayusculas

my_other_set.remove("Constanza")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

# del my_other_set
# print(my_other_set) #error porque ya no existe

my_set = {"Constanza", "Salinas", 29}#puedo pasar un set a lista, esto la ordena
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))#es como restar, se elimino my_set del set