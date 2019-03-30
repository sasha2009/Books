a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x: x ** 2, a)

even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)
