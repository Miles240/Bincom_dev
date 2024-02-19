def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


# Calculate the first 50 Fibonacci numbers
fib_numbers = fibonacci(50)

# Sum the first 50 Fibonacci numbers
fib_sum = sum(fib_numbers)

print("Sum of the first 50 Fibonacci numbers:", fib_sum)
