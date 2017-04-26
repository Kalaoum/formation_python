maliste = [1,2,3,4,5]

squared = []
for i in maliste:
    squared.append(i**2)
print("APPEND",squared)

squared = list(map(lambda x:x**2,maliste))
print("MAP",squared)

#Filter
nombre = range(-5,5)
moins_que_zero = list(filter(lambda x:x < 0, nombre))
print("Filter:", moins_que_zero)

moins_que_zero = [ a for a in nombre if a < 0 ]
print("En Instension:", moins_que_zero)

from functools import reduce
product = reduce((lambda x, y: x * y), [1,2,3,4])

print("REDUCE",product)