def cube(number):
	return number ** 3

mynums = [12, 14, 16, 13, 7]

mapcube = map(cube, mynums)

print(mapcube)
