#Data files
'''
f = open("filename.extension", "r")         #Abre un documento para lectura
f.readline()                                #Lee una linea del archivo
lines_list = f.readlines()
for line in lines_list                      #Se puede iterar con la info del archivo
    print("line read" + line)
f = open("filename.extension", "w")         #Abre un documento para escritura
f.close()                                   #Cierra el archivo
with open("filename.extension", "r") as f:  #Utiizando with al salir del bloque el archivo se cierra
    lines_list = f.readlines()
    for line in lines_list
        print("line read" + line)
'''

#Reading a file and some methods
'''
with open("olympics.txt", "r") as f:
    lines = f.readlines()
    for line in lines[:11]:
        print(line.strip())

olypmicsfile = open("olypmics.txt", "r")
for aline in olypmicsfile.readlines():
    values = aline.split(",")               #Crea una lista por cada linea y la imprime
    print(values[0], "is from", values[3], "and is on the roster for", values[4])
olypmicsfile.close()
        
filevar.write(astring)                      #Añade "astring" al final de "filevar"
filevar.read(n)                             #Lee y regresa un string de n caracteres
filevar.readline()                          #Lee y regresa la siguiente linea del archivo 
filevar.readlines(n)                        #Regresa una lista de str, n determina los chr pero se regresa la linea completa

with open("school_prompt2.txt", "r") as f:
    num_char = len(f.read())                #Asigna a num_char el total de char en el archivo
    print(num_char)
    
with open("travel_plans2.txt", "r") as f:
    num_lines = len(f.readlines())          #Asigna a num_lines el numero de elementos de la lista
    print(num_lines)

with open("emotion_words2.txt", "r") as f:
    first_forty = f.read(40)                #Asigna a first_forty un string de 40 char
    print(first_forty)

with open("emotion_words.txt", "r") as f:
    num_lines = 0
    for line in f.readlines():              #Se usa un paatron acumulativo para contar las lineas totales
        num_lines += 1
    print(num_lines)
'''

#Write a file
'''
filename = "squares.txt"
outfile = open(filename, "w")

for number in range(16):
    square = number * number
    outfile.write(str(square) + "\n")
outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()
'''

#CSV (Comma-Separated Values)
'''
fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport' + '\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    #row_string = ','.join(olympian[0], str(olympian[1]), olympian[2])
    #Si todos los elementos fueran str:
    #row_string = ','.join(olympian)
    outfile.write(row_string + '\n')
outfile.close()

with open('reduced_olympics.csv', "r") as f:
    competitors = f.read()
    print(competitors)

#Guarda y muestra la tercer palabra de cada elemento de la lista
lista = ["Perro de cadena gruesa", "Tengo marcada la esquina", "Soy un pitbull de pelea, mandibula asesina",
         "Soy el chef, el mejor en la cocina", "A la verga con su beef, me gusta la cecina", ""]
three = []
for sentence in lista[:-1]:
    word = sentence.split()
    three += [word[2]]
print(three)

#Guarda, compara y muestra las palabras que contenan el caracter "p"
p_words = []
with open("school_prompt2.txt", "r") as f:
    text = f.read()
    print(text)
    sentences = text.split('\n')
    print(sentences)
    for word in sentences:
        y = word.split()
        for x in y:            
            if 'p' in x:
                p_words += [x]
print(p_words)
'''