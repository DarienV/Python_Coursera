#Functions definitions
'''
import math

def triangulo (l1, l2, l3):
    P = l1 + l2 +l3
    c = math.sqrt(l1**2 + l2**2)
    if c == l3:
        print("Este es un triangulo rectangulo")
        print("Sus dimensiones son {}, {}, {} y  su perimetro {}".format(l1,l2,l3,P))
    else:
        print("Este no es un triangulo rectangulo")

triangulo(4,3,5)
'''

#Global variables
'''
n = 4
def pow (m):
    x = m ** n      #Hace uso de una variable global en un espacio local
    return x

print(pow(2))

def pow1(a,b):
    y = a ** b
    return y

print(pow1(2,4))
'''

#Side Efects
'''
def chng(lst):
    lst[0] = 'Adios'
    return lst

def unchng(lst):
    nlst = lst[:]
    nlst.append('Nuevo elemento')
    return nlst

list1 = ['Hola', 'Mundo']
list2 = list1[:]

print(list1)
print(list2)
print('Ejecutamos las funciones y asignamos la nueva lista a una variable')
chng(list1)
unchng(list2)
x = unchng(list2)
print(list1)
print(list2)
print(x)
'''

#Tuplas
'''
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
    
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for x in pokemon.items():
    p_names.append(x[0])
    p_number.append(x[1])

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z))


'''