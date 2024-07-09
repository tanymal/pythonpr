def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    result_add = add(1, 2)
    result_subtract = subtract(5, 3)
    result_multiply = multiply(4, 2)
    result_divide = divide(8, 4)
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")
    print(f"Multiplication result: {result_multiply}")
    print(f"Division result: {result_divide}")
