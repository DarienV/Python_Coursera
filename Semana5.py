#Sort and Sorted methods
"""
lst1 = [9, 7, 11, 15, 22, 69, 35]
lst2 = ['Darien', 'Cesar', 'Eros', 'Alejandrina', 'Raul', 'Maria']

lst1.sort()
print(lst1)
print(sorted(lst2, reverse = True))
"""

"""
L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute)
print(L2)

#or in reverse order
print(sorted(L1, reverse=True, key=absolute))
"""

"""
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

d = {}
for x in L:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
for x in sorted(d.keys(), reverse = True, key = lambda k: d[k]):
    print("{} appears {} times".format(x, d[x]))
"""

"""
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)
"""

"""

def last_four(x):
    y = str(x)
    return y[-4:]

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key = last_four)
"""

"""
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key = lambda x: str(x)[-4:])
"""