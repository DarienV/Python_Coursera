#The While Loop
#Tabla de x numero
"""def tabla(x):
    accum = 1
    while accum <= 10:
        val = accum * x
        val = str(val)
        accum = str(accum)
        x = str(x)
        print(x + " x " + accum + "= " + val)
        accum = int(accum)
        x = int(x)
        accum += 1

x = input("Ingresa un numero para imprimir su tabla: ")
x = int(x)
tabla(x)"""

#Listener loop
"""
def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
"""

"""
def get_yes_or_no(message):
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')
"""

"""
import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(50)

wn.exitonclick()
"""

#Break & Continue statements
"""
while True:
    orden = input("¿Desea salir del ciclo? S o N: ")
    orden.upper()
    if orden == 'S':
        print("Salio del ciclo.")
        break
    if orden == 'N':
        print("Sigue en el ciclo.\n")
        continue
"""

#Define una función para agregar los elementos de una lista de str a una sublista
#hasta que se encuentre con el str "bye" y que no exceda los 10 elementos
"""
def beginning(lst):
    a = 0
    sub = []
    while lst[a] != "bye":
        sub.append(lst[a])
        a += 1
        if a == 10:
            break
    return sub
"""

"""
names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))
"""

#Lambda functions
"""
def cuadrado(x):
    return x*x

cuadrado2 = lambda x: x*x

print(cuadrado(2), cuadrado2(4))
"""