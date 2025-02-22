import math
R = 1000
C = 0.001

def f(x):
    return C*(1 - math.exp(-x/(R*C))) - 0.9*C

def df(x):
    return math.exp(-x/(R*C))/R

def main():
    x0 = 0
    xk = x0 - f(x0)/df(x0)
    e = 0.0001
    er = abs(xk - x0)/abs(xk)
    while er > e:
         x0 = xk
         xk = x0 - f(x0)/df(x0)
         er = abs(xk - x0)/abs(xk)

    print(xk)

main()