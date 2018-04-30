from utilities import prime_number_check
from utilities import digit_count

'''def right_to_left_truncatability_check(num):

	while num > 0:
		if prime_number_check(num) == 0:
			return 0

		num = num // 10
	return 1


def left_to_right_truncatability_check(num):

	count = digit_count(num)

	while count > 0:
		if prime_number_check(num) == 0:
			return 0

		num = num % (10 ** (count - 1))
		count -= 1 

	return 1'''

def truncatability_check(num):

	left_trunk = num
	right_trunk = num

	count = digit_count(num)

	while right_trunk > 0:
		if prime_number_check(right_trunk) == 0 or prime_number_check(left_trunk) == 0:
			return 0

		right_trunk = right_trunk // 10
		left_trunk = left_trunk % (10 ** (count - 1))

		count -= 1

	return 1


def main():

	count = 0 # Keep track of the number of truncatable primes (11 in total)
	sum = 0
	i = 10

	while count < 11:
		if truncatability_check(i) == 1:
			print(i)
			count += 1
			sum += i

		print(i)
		i += 1

	print("Sum of Truncatable Primes = " + str(sum))

if __name__ == '__main__':
	main()