""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    total = 0
    for num in numbers.split(","):
        total += int(num)
    return total


