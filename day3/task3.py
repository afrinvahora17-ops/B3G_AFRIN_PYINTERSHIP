numbers = [12, 45, 23, 12, 67, 45, 89, 23, 10, 67, 34, 89, 50, 10, 75]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)