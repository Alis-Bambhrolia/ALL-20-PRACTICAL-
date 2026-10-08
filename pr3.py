num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is odd number")

mark = int(input("Enter marks: "))
if mark >= 80 and mark <= 100:
    print("Grade: A")
if mark >= 60 and mark < 80:
    print("Grade: B")
if mark >= 40 and mark < 60:
    print("Grade: C")
if mark < 40 and mark >= 0:
    print("Fail")

mark = int(input("Enter marks: "))
if mark >= 80 and mark <= 100:
    print("Grade: A")
elif mark >= 60 and mark < 80:
    print("Grade: B")
elif mark >= 40 and mark < 60:
    print("Grade: C")
else:
    print("Fail better luck next time")

for i in range(1, 11):
    if i == 5:
        break
    print(i)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

for i in range(1, 6):
    if i % 2 == 0:
        pass
    else:
        print(i)