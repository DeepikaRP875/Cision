# 6.	Sum of Even Fibonacci Numbers
# Write a program to calculate the sum of the first 100 even-valued Fibonacci numbers. Consider efficiency and demonstrate good coding practices.

def sum_even_fibonacci(n):
    sum_even = 0
    num_even_fib = 0
    a, b = 0, 1
    while num_even_fib < n:
        a, b = b, a + b
        if b % 2 == 0:
            sum_even += b
            num_even_fib += 1
    return sum_even

# Calculate the sum of the first 100 even-valued Fibonacci numbers
result = sum_even_fibonacci(100)
print(f"The sum of the first 100 even-valued Fibonacci numbers is: {result}")