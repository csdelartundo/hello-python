###Manejo de errores###

num_one = 5
num_two = 1
num_two = "1"

#try except
try:
    print(num_one + num_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")

#try except else finally
try:
    print(num_one + num_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: #opcional, si se ejecuta un except el else no se ejecuta
    print("La ejecución continúa correctamente")
finally: #opcional, se ejecuta siempre
    print("La ejecución continúa")

#excepciones por tipo
try:
    print(num_one + num_two)
    print("No se ha producido un error")

except TypeError: #error de tipo
    #se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")

#captura de la informacion de la excepcion

try:
    print(num_one + num_two)
    print("No se ha producido un error")
except ValueError as error: #error de valor
    #se ejecuta si se produce una excepcion
    print(error)
except Exception as error: #error general
    print(error)