import math
import random
import statistics as st

def calculate_product(val1, val2):
    return val1 * val2

result = calculate_product(6, 7)
print("Product of 6 and 7 is:", result)

def show_message():
    print("It is python for Data Science lab")

show_message()

def display_diff(num1, num2):
    print(f"Difference between {num1} and {num2} is: {num1 - num2}")

display_diff(26, 9)

def compute_sum():
    p = float(input("Enter 1st num: "))
    q = float(input("Enter 2nd num: "))
    return p + q

total = compute_sum()
print("Calculated Sum:", total)

def render_profile(username, role="Data Analyst"):
    print(f"User: {username} | Role: {role}")

render_profile("Rahul")
render_profile("Priya", "Data Scientist")

def display_course_info(course_code, course_name):
    print(f"Course [{course_code}]: {course_name}")

display_course_info(course_name="PDS", course_code="123")

val = float(input("Enter a float number: "))
print("Square Root:", math.sqrt(val))
print("Squared Power:", math.pow(val, 2))
print("Ceiling Value:", math.ceil(val))
print("Floor Value:", math.floor(val))
print("Value of Pi:", math.pi)

dataset = [15, 25, 35, 45, 55, 65]
print("Random Integer (1-50):", random.randint(1, 50))
print("Random Choice:", random.choice(dataset))
random.shuffle(dataset)
print("Shuffled List:", dataset)

scores = [78, 85, 92, 85, 88, 90, 85]
print("Dataset:", scores)
print(f"Mean Score: {st.mean(scores):.2f}")
print("Median Score:", st.median(scores))
print("Mode Score:", st.mode(scores))