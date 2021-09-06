a, b = 1, 2
value = a + b
fib = [a, b, value]
limit = 4 * (10 ** 6)

while value < limit:
    a, b = b, value
    value = a + b
    fib.append(value)

evenFib = [num for num in fib if not num % 2]
print(sum(evenFib))
