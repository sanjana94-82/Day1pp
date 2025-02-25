def closest_to_zero(numbers):
    return min(numbers, key=lambda x: (abs(x), -x))


numbers = [3, -4, 2, -1, -2, 5, -3]
result = closest_to_zero(numbers)
print(result)
