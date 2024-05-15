def squares_list():
    squares = []

    for num in range(1, 31):
        square = num ** 2
        squares.append(square)

    return squares

squares = squares_list()

print("List of squares from 1 to 30:", squares)