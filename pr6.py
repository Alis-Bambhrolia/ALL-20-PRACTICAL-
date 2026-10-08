def perform_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid data type for division.")
    else:
        print(f"Division Successful! Result: {result}")
    finally:
        print("Execution of division block completed.\n")

perform_divide(20, 4)
perform_divide(10, 0)

class InvalidAgeException(Exception):
    pass

def check_if_vote(age):
    try:
        if age < 18:
            raise InvalidAgeException("Age must be 18 or above to vote.")
        else:
            print(f"Age {age}: Eligible to vote.")
    except InvalidAgeException as e:
        print(f"Custom Exception Caught: {e}")

check_if_vote(21)
check_if_vote(16)