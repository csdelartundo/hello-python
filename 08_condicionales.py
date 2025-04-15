###Condicionales###

my_condition = True
if my_condition:
    print("Se ejecuta la condición del primer if")

my_condition = 5 * 5
if my_condition == 10:
    print("El resultado es 10")
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual a 20")
#al estar fuera del if y else se ejecutara siempre, al tabular se podria ejecutar dependiendo de la condicion
print("La ejecucion continua")

my_string = ""
if not my_string:
    print("Mi cadena de texto es verdadera")
if my_string == "mi cadena de textooooo":
    print("Mi cadena de texto es igual a mi cadena de texto")