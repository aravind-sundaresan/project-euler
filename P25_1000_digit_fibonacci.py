def fibo():
	a = 1
	b = 1
	count = 2

	#while(len(str(b)) < 1000):
	while(b < 10**999):
		a, b = b, a + b

		count += 1
		print(count)

	return count

if __name__ == "__main__":
	count = fibo()
	print(count)