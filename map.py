numbers = (1, 2, 3, 4)


def square(numbers):
    return numbers * numbers


result = list(map(square, numbers))
print(result)
