import random 
list = [random.randint(1,10) for _ in range(10)]
counter = {}

for elem in list:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)

print (list)