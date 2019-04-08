import math

def bisect(a, b, ep, max_iterate, f):

    left = f(a)
    right = f(b)
    count = 0

    if left*right > 0:
        print("No solution!")
        return False
    if left == 0:
        print("A Solution is: ", a)
    if right == 0:
        print("A Solution is: ", b)

    while abs(b - a) > ep and count < max_iterate:
        mid = (a + b)/2.0
        m = f(mid)
        if m == 0:
            print("A Solution is ", mid)
            return mid
        elif left * m < 0:
            b = mid
            count += 1
            print(count,mid)
        else:
            m * right > 0
            a = mid
            count += 1
            print(count,mid)
    return mid

f = lambda x: x**5 - x**4 + x - 1
val = bisect(-1000000, 1000000, 0.000000001, 20, f)
print("Result is ", val)

f = lambda x: x - math.e**(-x)
val = bisect(-1, 1.5, 0.000000001, 20, f)
print("Result is ", val)