def add_numbers(array):
    # array = [1.0, 1.1, "1"]
    x = 0
    for num in array:
        x += float(num)
    return x
result = add_numbers([1.0, 1.1, "1"])
print(result)

