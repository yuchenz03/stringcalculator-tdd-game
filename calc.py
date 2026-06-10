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
        total += int(num)
    return total


