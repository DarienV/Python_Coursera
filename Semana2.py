#Diccionarios
'''
#USA has 33 gold medals, 17 silver, and 12 bronze
medals = {"gold" : 33, "silver": 17, "bronze" : 12}

#Italy has 7 gold medals, 8 silver metals, and 6 bronze
olympics = {}
olympics["gold"] = 7
olympics["silver"] = 8
olympics["bronze"] = 6
#Italy has won 4 more silver medals so:
olympics["silver"] = olympics["silver"] + 4
'''

#Dictionary Methods
'''
#dic.keys()                 Returns a view of the keys in the dictionary
#dic.values()               Returns a view of the values in the dictionary
#dic.items()                Returns a view of the key-value pairs in the dictionary
#dic.get(key)               Returns the value associated with key; None otherwise
#dic.get(key, alt val)      Returns the value associated with key; alt otherwise

#Si se necesita hacer .keys(), . values() y .items() una lista de estos valores; list(dic.keys())

inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))

'''

#Dictionary Accumulation
'''
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

#print("t: " + str(letter_counts['t']) + " occurrences")
#print("s: " + str(letter_counts['s']) + " occurrences")
#print("d: " + str(letter_counts['d']) + " occurences")

for k in letter_counts.keys():
    print(k, letter_counts[k])

f = open('scarlet2.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
    if c not in letter_counts:
        # we have not seen this character before, so initialize a counter for it
        letter_counts[c] = 0

    #whether we've seen it before or not, increment its counter
    letter_counts[c] = letter_counts[c] + 1

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

tot = 0
for letter in letter_counts:
    if letter in letter_values:
        tot = tot + letter_values[letter] * letter_counts[letter]

print(tot)

#Examen
#Peor letra (menos apariciones)
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
worst_num = 5000
worst_char =''

for ch in sally:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for x in characters.keys():
    if worst_num > characters[x]:
        worst_num = characters[x]
        worst_char = x
print(worst_char, worst_num)

#Mejor letra (mas apariciones)
sally = "sally sells sea shells by the sea shore"
characters = {}
best_num = 0

for ch in sally:
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for x in characters.keys():
    if best_num < characters[x]:
        best_num = characters[x]
        best_char = x
print(best_char, best_num)
'''