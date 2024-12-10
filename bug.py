def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /'")
        return None

# This will raise a TypeError
print(function_with_uncommon_error(10, 'a'))
# This will raise a ZeroDivisionError
print(function_with_uncommon_error(10, 0))