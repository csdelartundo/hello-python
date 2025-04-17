###Clases###
#en estos casos las clases se escriben en camelcase
class MyEmptyPerson:
    pass #para poder dejar la clase vacia

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        self.full_name = f"{name} {surname} {alias}"
        self.__name = name #propiedad privada, solo se puede acceder desde dentro de la clase

    def get_name(self):
        return self.__name #para acceder a ella se deberia hacer un set

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Constanza", "Salinas")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Constanza", "Salinas", "Whitezoe")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León El Loco"
print(my_other_person.full_name)