
def palindrome_check(str):

	length = len(str)

	i, j = 0, (length - 1)

	for i in range(length // 2):
		if str[i] != str[j]:
			return 0

		j -= 1

	return 1


def compute_factorial(num):
	
	factorial = 1

	for i in range(2, num + 1):
		factorial *= i

	return factorial


def prime_number_check(num):

	for i in range(2, (num // 2 + 1)):
		if num % i == 0:
			return 0

	return 1


def find_factors(num):
	
	factors = [1]

	for i in range(2, (num // 2 + 1)):
		if num % i == 0:
			factors.append(i)

	factors.append(num)

	return factors

if __name__ == '__main__':
	main()