""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    
    numbers = numbers.replace("\n", ",")
    delim = ","
    if numbers[0:2] == "//":
        delim = numbers[2]
        numbers = numbers[4:]

    total = 0
    numbers = numbers.replace(delim, ",")
    for num in numbers.split(","):
        if int(num) < 0:
            raise ValueError(f"negatives not allowed: {num}")
        total += int(num)
    return total


