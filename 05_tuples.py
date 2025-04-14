###Tuples###
# Ordenada.
# Inmutable (no puedes modificarla luego de crearla).
# Permite duplicados.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (29, 1.59, "Constanza", "Salinas", "Cota")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(29))
print(my_tuple.index("Constanza"))

# my_tuple[1] = 1.80 #error por ser inmutable
# print(my_tuple)

print(my_tuple + my_other_tuple)

new_tuple = my_tuple + my_other_tuple
print(new_tuple)
print(new_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Whitezoe"
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple #elimina la variable
print(my_tuple) #error porque ya no existe