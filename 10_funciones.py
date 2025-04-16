###Funciones###

def my_function():
    print("Esto es una función")

my_function()

def sum_values(first_value, second_value, third_value: int):
    print(first_value + second_value + third_value)

sum_values(5, 7, 7) 
sum_values(1.4, 5.2, 0)
sum_values("hola ", "adios ", "python")

def sum_two_values_return(first_value, second_value):
    return first_value + second_value
sum_two_values_return(10, 5)

my_result = sum_two_values_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}") #f-string, accede a los valores que se van a concatenar

print_name(surname = "Salinas", name = "Constanza") #se puede cambiar el orden

def print_name_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_default("Constanza", "Salinas", "Whitezoe")

def print_texts(*texts): #se puede pasar cualquier numero de parametros
    for text in texts: #itera sobre cada texto
        print(text.upper())
print_texts("hola", "adios", "python")