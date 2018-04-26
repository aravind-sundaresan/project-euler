from numpy import genfromtxt
from math import log

if __name__ == '__main__':
	
	filename = "p099_base_exp.txt"

	base_exponent_pairs = genfromtxt(filename, delimiter=',')

	log_exponentials = []

	for pair in base_exponent_pairs:
		base = pair[0]
		exponent = pair[1]

		log_exponential = exponent * log(base)

		log_exponentials.append(log_exponential)

	largest_exponential = max(log_exponentials)
	print("Largest exponential = " + str(largest_exponential))
	
	line_number = log_exponentials.index(largest_exponential) + 1
	print("Line number = " + str(line_number))

