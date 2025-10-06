def classify_grades(grades):
	excellent = []
	good = []
	passed = []
	failed = []

	for g in grades:
		if g >= 90:
			excellent.append(g)
		elif 70 <= g <= 89:
			good.append(g)
		elif 50 <= g <= 69:
			passed.append(g)
		else:
			failed.append(g)

	return excellent, good, passed, failed


if __name__ == "__main__":
	grades = [95, 82, 67, 54, 100, 73, 88, 42]
	excellent, good, passed, failed = classify_grades(grades)

	print("excellent:", excellent)
	print("good:", good)
	print("pass:", passed)
	print("fail:", failed)

