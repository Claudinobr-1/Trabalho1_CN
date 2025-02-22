import math
R = 1000
C = 0.001

def f(x):
    return C*(1 - math.exp(-x/(R*C))) - 0.9*C

def main():
    a = 0
    b = 10
    e = 0.0001
    while abs(b - a) > e:
        x = (a + b)/2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    
    print(x)

main()