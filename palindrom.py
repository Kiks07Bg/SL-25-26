def find_palindromes(words):
	palindromes = []
	for w in words:
		if w == w[::-1]:
			palindromes.append(w)
	return palindromes

if __name__ == "__main__":
	words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
	palindromes = find_palindromes(words)
	print("palindromes:", palindromes)

