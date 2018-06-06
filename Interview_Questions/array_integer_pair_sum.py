
def integer_pair_sum(array, sum):

	dict = {}

	for i in range(len(array)):
		dict[i] = array[i]

	for i in range(len(array)):
		complement = sum - dict[i]
		if complement in dict.values():
			print(str(array[i]) + " " + str(complement))


if __name__ == '__main__':

	array = [2, 4, 3, 5, 7, 8, 9]
	required_sum = 8

	integer_pair_sum(array, required_sum)