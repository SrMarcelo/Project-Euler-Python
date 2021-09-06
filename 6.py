numbers = [num for num in range(1, 101)]
sumOfSquares = sum([num ** 2 for num in numbers])
squareOfSum = sum(numbers) ** 2

print(squareOfSum - sumOfSquares)
