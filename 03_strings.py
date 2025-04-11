###Strings###

my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un string \n escapado"
print(my_scape_string)

###Formateo###

name, surname, age = "Constanza", "Salinas", 29
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))

name, surname, age = "juan", "perez", 24 
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

#esta forma es la mas correcta, impide que se imprima algo que no corresponda
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))

###Inferencia de datos###

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

###Desempaquetado de caracteres###

language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

###División###

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

###Reverse###

reversed_language = language[::-1]
print(reversed_language)

###Funciones###

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("on"))
print("Py" == "py") #no es lo mismo