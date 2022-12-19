def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Inside result: {}".format(result))
    return result
