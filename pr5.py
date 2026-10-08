import csv
import pickle

with open("sample.txt", "w") as file:
    file.write("1 System Initialized.\n")
    file.write("2 Processing Data.\n")

with open("sample.txt", "a") as file:
    file.write("3 Task completed.\n")

print("--- Text file content ---")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

data = [
    ["ID", "Name", "Score"],
    ["1", "Dharmik", 9.7],
    ["2", "Krish", 8.7]
]

with open("file1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("file1.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["3", "Manan", 6.5])

print("--- CSV file content ---")
with open("file1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

student = {"roll_no": 1, "name": "XYZ", "marks": [85, 90, 70]}

with open("Student.dat", "wb") as file:
    pickle.dump(student, file)

print("--- Binary file content ---")
with open("Student.dat", "rb") as file:
    record = pickle.load(file)
    print("Data:", record)