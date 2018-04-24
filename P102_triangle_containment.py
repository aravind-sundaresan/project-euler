from numpy import genfromtxt 

def compute_triangle_area(x1, y1, x2, y2, x3, y3):
	area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
	return area

if __name__ == '__main__':
	
	filename = "p102_triangles.txt"

	coordinates = genfromtxt(filename, delimiter=',')

	count = 0
	for triangle in coordinates:
		# Compute area of the triangle
		area_triangle = compute_triangle_area(int(triangle[0]), int(triangle[1]), int(triangle[2]), int(triangle[3]), int(triangle[4]), int(triangle[5]))
		
		# Compute area of the sub triangles
		area_triangle_1 = compute_triangle_area(int(triangle[0]), int(triangle[1]), int(triangle[2]), int(triangle[3]), 0, 0)
		area_triangle_2 = compute_triangle_area(int(triangle[2]), int(triangle[3]), int(triangle[4]), int(triangle[5]), 0, 0)
		area_triangle_3 = compute_triangle_area(int(triangle[4]), int(triangle[5]), int(triangle[0]), int(triangle[1]), 0, 0)

		if (area_triangle == (area_triangle_1 + area_triangle_2 + area_triangle_3)):
			count += 1

	print(count)
