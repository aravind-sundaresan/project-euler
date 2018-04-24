
def reverse_number(num):

	reverse = 0
	while num > 0:
		digit = num % 10
		reverse = reverse * 10 + digit
		num = num // 10

	return reverse

def check_reversible(sum_num_reverse):

	while sum_num_reverse > 0:
		digit = sum_num_reverse % 10
		
		if digit % 2 == 0:
			return 0

		sum_num_reverse = sum_num_reverse // 10

	return 1

if __name__ == '__main__':

	reversible_numbers = set()

	for i in range(1, 1001):
		reverse = reverse_number(i)
		
		if (i > 10 and reverse > 10):
			sum_num_reverse = i + reverse

		
			if check_reversible(sum_num_reverse) == 1:
				print(str(i) + "," + str(reverse))
				reversible_numbers.add(i)
				reversible_numbers.add(reverse)

	print(reversible_numbers)
	print(len(reversible_numbers))

