a = 25
b = 10.5
c = "Student"
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

x = 10
x += 5
print("x += 5:", x)
x *= 2
print("x *= 2:", x)

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("d and False:", d and False)
print("d or False:", d or False)
print("not d:", not d)

nums = [10, 20, 30, 40]
print("20 in nums:", 20 in nums)
print("50 not in nums:", 50 not in nums)

p = [1, 2]
q = [1, 2]
r = p

print("p is r:", p is r)
print("p is q:", p is q)
print("p is not q:", p is not q)

m = 6
n = 3
print("m & n:", m & n)
print("m | n:", m | n)
print("m ^ n:", m ^ n)
print("~m:", ~m)
print("m << 1:", m << 1)
print("m >> 1:", m >> 1)