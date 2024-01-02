import math

def f(x):
    return math.sin(x) * math.cos(x)

def num_integra(f, a, b, num):
    h = (b - a) / num
    x = [a + i * h for i in range(num+1)]
    y = [f(x[i]) for i in range(num+1)]
    return h * (sum(y) - 0.5 * (y[0] + y[num]))

a = 0
b = 4 * math.pi
num = 1000

area = num_integra(f, a, b, num)
if area < 0:
    area = -area

print("Approximate area:", area)