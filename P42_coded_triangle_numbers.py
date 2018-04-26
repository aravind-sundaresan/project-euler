def generate_triangle_numbers(n):

	triangle_numbers = []
	for i in range(1, n+1):

		triangle_number = (i * (i + 1)) // 2
		triangle_numbers.append(triangle_number)


	return triangle_numbers


if __name__ == '__main__':
	
	filename = "p042_words.txt"
	file_pointer = open(filename, "r+")

	count = 0

	triangle_numbers = generate_triangle_numbers(100)

	words = file_pointer.read().split(',')
	print(len(words))

	for word in words:

		word = word[1:-1] # Trim the quotes from the beginning and end of the words

		word_value = [ (ord(c) - (65 - 1)) for c in word ] # Obtaining the alphabet number by subtracting 65 from the ASCII value of the character

		if sum(word_value) in triangle_numbers:
			count += 1
			print(word + " " + str(sum(word_value)))
	
	print("Number of Triangle Words = " + str(count))