numbers = [5, 12, 18, 21, 33, 42, 50, 77, 90]
special_numbers = []

for num in numbers:
	if num > 20 and num % 3 == 0 and num % 5 != 0:
		special_numbers.append(num)

print("special_numbers:", special_numbers)