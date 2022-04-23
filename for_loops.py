# Your code below:
single_digits = list(range(10))
squares = []
cubes = [digit**3 for digit in single_digits]

for digit in single_digits:
  #print(digit)
  squared_digit = digit ** 2
  squares.append(squared_digit)
print(squares)
print(cubes)
