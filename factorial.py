def factorial(n):
    """Return the factorial of a positive integer."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # outputs: 120
