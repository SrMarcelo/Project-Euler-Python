number = 600851475143
primeFactors = []
i = 2
while i <= number:
    if not number % i:
        number /= i
        primeFactors.append(i)
    i += 1

print(max(primeFactors))
