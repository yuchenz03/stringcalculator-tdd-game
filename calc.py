""" Edit the function below to implement the String Calculator TDD Kata """

def add(numbers):
    if numbers == "":
        return 0
    total = 0
    numbers = numbers.replace("\n", ",")
    for num in numbers.split(","):
        total += int(num)
    return total


