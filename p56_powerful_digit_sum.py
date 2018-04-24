
def calculate_digit_sum(num):

	digit_sum = 0

	while num > 0:
		digit = num % 10
		digit_sum += digit

		num = num // 10

	return digit_sum

if __name__ == '__main__':
	
	digit_sums = []

	for i in range(2, 100):
		for j in range(2, 100):
			num = i ** j
			digit_sum = calculate_digit_sum(num)

			#print(str(num) + " " + str(digit_sum))
			digit_sums.append(digit_sum)

	print("Powerful Digit Sum = " + str(max(digit_sums)))

