x = [10, 30, 20]
print("The data type of x:", type(x))
print("List x is:", x)

x.append(40)
print("List x after append:", x)

y = x.copy()
print("Copy list via copy method:", y)
print("List x count of 10 is:", x.count(10))

z = [45, 55, 67, 87]
x.extend(z)
print("List x after extend:", x)
print("Index of 40 in list x:", x.index(40))

x.insert(3, 100)
print("After insert method:", x)

x.pop()
print("After pop method:", x)

x.reverse()
print("After reverse method:", x)

x.sort()
print("List x after sort:", x)

x.clear()
print("List x after clear method:", x)

s = {1, 2, 3}
print("The data type of s is:", type(s))
print("S is set:", s)

s.add(7)
print("S after add(7):", s)

s1 = s.copy()
print("Copy of s in s1:", s1)

s2 = {9, 15, 8, 17}
print("S - S2:", s.difference(s2))

s.discard(2)
print("After discard(2) s:", s)
print("S after intersection with S2:", s.intersection(s2))
print("S after isdisjoint:", s.isdisjoint(s2))
print("S after issubset:", s.issubset(s2))
print("S after issuperset:", s.issuperset(s2))

popped_item = s.pop()
print("S after pop method:", s)

s.remove(3)
print("S after remove method:", s)

s.clear()
print("S after clear method:", s)

t = (5, 7, 9, 10)
print("Data type of tuple is:", type(t))
print("Tuple t:", t)
print("Tuple after count method:", t.count(7))
print("Tuple after using index method:", t.index(10))

d = {"name": "Dharmik", "year": "3", "sem": "5"}
print("The data type of d:", type(d))
print("The dictionary is:", d)
print("Get value using get():", d.get("name"))
print("Use dictionary items():", d.items())
print("Dictionary keys():", d.keys())
print("Dictionary values():", d.values())

d.pop("sem")
print("Pop the item in dictionary:", d)

d.update({"Enroll": 163})
print("Updated dictionary:", d)

x = "Hello world"
print("X is:", type(x))
print("X contained:", x)
print("X's uppercase:", x.upper())
print("X's lowercase:", x.lower())
print("X after capitalize:", x.capitalize())
print("X after title:", x.title())
print("X after replace:", x.replace("Hello", "Hi"))

x = x.replace("Hello", "Hi")
print("Position of Hi in x:", x.find("Hi"))
print("Position of o in x:", x.index("o"))