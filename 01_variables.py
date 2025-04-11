###Variables###
#las variables no se escriben con camelcase, todo en minuscula o snakecase
my_variable = "My string variable" 
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_variable)) #len viene de lenght, cuenta los caracteres

#Variables en una sola linea
name, surname, alias, age = "Constanza", "Salinas", "Cota", 29
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

#Inputs
#name = input("¿Cuál es tu nombre?: ")
#age = input("¿Cuántos años tienes?: ")

print(name)
print(age)

#Cambio de tipo de dato
name = 35
age = "Constanza"

print(name)
print(age)

print(type(name))
print(type(age))

#forzando el tipo de dato
address: str = "mi direccion"
address = 32
print(address)
