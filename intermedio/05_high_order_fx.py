###Funciones de orden superior###
from functools import reduce

def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Clousure ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clousure = sum_ten(1)
print(add_clousure(5))

sum_ten(5)(1) 

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30] 

# Map
def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

#Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

#Reduce/total acumulado

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))   