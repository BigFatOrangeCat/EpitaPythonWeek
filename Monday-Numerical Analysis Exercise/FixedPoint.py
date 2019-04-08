import math

g = lambda x: 1 + .3 * math. sin(x)


def fixedpoint(a0, errorBd, maxIter, g):
	count = 0
	temp = a0
	an = g(a0)
	error = an-temp
	while (error > errorBd) and (count < maxIter):
		temp = an
		an = g(an)
		count += 1
		error = abs(an-temp)
		print(count, an, temp, error)
	return an

val = fixedpoint(1, 0.0000000001, 20, g)
#print("Result is ", val)
		