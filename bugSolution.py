def improved_function_with_error_handling(a, b):
    try:
        if not isinstance(b, (int, float)):
            raise TypeError("Divisor must be a number")
        if b == 0:
            raise ZeroDivisionError("Divisor cannot be zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return float('inf') # Return infinity for improved clarity
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Demonstrate improved error handling
print(improved_function_with_error_handling(10, 'a'))
print(improved_function_with_error_handling(10, 0))
print(improved_function_with_error_handling(10, 2))