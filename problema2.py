import math

def f(x):
    return pow(x,5)-3*pow(x,3)+2*pow(x,2)-5*x+1

def df(x):
    return 5*pow(x,4)-9*pow(x,2)+4*x-5

def main():
    x0 = 1
    xk = x0 - (f(x0)/df(x0))
    er = abs(xk - x0)
    e= 0.000001
    while er > e:
         x0 = xk
         xk = x0 - (f(x0)/df(x0))
         er = abs(xk - x0)
    
    print(xk)

main()