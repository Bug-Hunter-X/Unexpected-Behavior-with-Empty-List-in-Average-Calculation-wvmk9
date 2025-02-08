def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / count
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") # This will print 0, which might not be the expected behavior if an empty list is not anticipated. 