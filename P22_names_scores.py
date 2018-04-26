
def main():

	filename = "p022_names.txt"

	file_pointer = open(filename, "r+")

	names = file_pointer.read().split(',')

	names = sorted(names) # Sort the names in alphabetical order

	i = 1 
	sum_name_scores = 0

	for name in names:

		name = name[1:-1] # Trim the quotes from the beginning and end of the word

		name_score = sum([ (ord(c) - 64) for c in name ]) # Get the character sum for each word
		name_score = name_score * i

		sum_name_scores += name_score
		i += 1

	print("total of all the name scores = " + str(sum_name_scores))


if __name__ == '__main__':
	main()