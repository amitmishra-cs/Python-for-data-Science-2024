def fibonacci(n):
    fibonacci_series = [0, 1]  # Starting with the first two terms of the series

    # Generating subsequent terms
    for i in range(2, n):
        next_term = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(next_term)

    return fibonacci_series

# Example usage:
num_terms = 10  # Change this value to generate Fibonacci series up to a different number of terms
fib_series = fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:", fib_series)

  