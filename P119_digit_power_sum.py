
def compute_digit_sum(num):

	digit_sum = 0
	
	while num > 0:
		digit_sum = digit_sum + (num % 10)
		num = num // 10

	return digit_sum

if __name__ == '__main__':
	
	count = 0

	digit_power_sum = []

	
	for i in range(2, 100):
		for j in range(2, 10):
			num = i ** j

			digit_sum = compute_digit_sum(num)

			if digit_sum == i:
				count += 1
				print(str(num) + " " + str(i) + " " + str(j))
				digit_power_sum.append(num)

	digit_power_sum = sorted(digit_power_sum)

	print("Solution is " + str(digit_power_sum[29]))

