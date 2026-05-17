import custom_math

# 1. Test basic execution
num = 10
result = custom_math.factorial(num)
print(f"Factorial of {num} via C Extension: {result}")

# 2. Inspect module properties
print(f"Module Name: {custom_math.__name__}")
print(f"Docstring: {custom_math.factorial.__doc__}")

# 3. Verify safety rails
try:
    custom_math.factorial(-5)
except ValueError as e:
    print(f"Caught expected error: {e}")
