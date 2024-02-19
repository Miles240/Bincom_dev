import random

def generate_random_binary():
    # Generate a random 4-digit binary number
    binary_num = ''.join(str(random.randint(0, 1)) for _ in range(4))
    return binary_num

def binary_to_decimal(binary_num):
    # Convert binary number to decimal
    decimal_num = int(binary_num, 2)
    return decimal_num

# Generate random binary number
random_binary = generate_random_binary()
print("Random Binary Number:", random_binary)

# Convert binary to decimal
decimal_number = binary_to_decimal(random_binary)
print("Decimal Equivalent:", decimal_number)
