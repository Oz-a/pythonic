import random
def cube(number):
	return number ** 3

mynums = [12, 14, 16, 13, 7]

mapcube = map(cube, mynums)

for cube in mapcube:
	print(cube)

print('Now moving over to multiplication \n\n')
def multiplier(a,b):
	return a*b

yournums = list(random.randint(1,20) for i in range(5))

print(yournums)

mapmult = map(multiplier, mynums, yournums)
for i in mapmult:
	print(i)
