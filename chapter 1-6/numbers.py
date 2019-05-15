for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)

even_numberes = list(range(2,11,2))
print(even_numberes)

squarses = []
for value in range(1,11):
    squarse = value**2
    squarses.append(squarse)
print(squarses)

squarses = []
for value in range(1,11):
    squarses.append(value**2)
print(squarses)

digits = list(range(1,10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

squarses = [value**2 for value in range(1,11)]
print(squarses)
