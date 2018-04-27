def main():

	# Formula for total number of rectangles in an M x N grid is: ((M * (M+1)) / 2) * ((N * (N+1)) / 2) 

	area_of_rectangle = 1
	min_difference = 2000000

	for m in range(100):  # Choose random range for m
		for n in range(m):
			
			count_rectangles = ((m * (m + 1)) / 2) * ((n * (n + 1)) / 2)
			difference = abs(2000000 - count_rectangles) 
			
			# Find the count closest to 2 million
			if difference < min_difference: 
				min_difference = difference
				print(str(m) + "," + str(n))
				area_of_rectangle = m * n

	print("Area of the rectangular grid = " + str(area_of_rectangle))

if __name__ == '__main__':
	main()