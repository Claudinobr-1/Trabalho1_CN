import math
R = 1000
C = 0.001
Q = 1 #Adotando o valor da carga máxima como 1C

def f(x):
    return Q*(1 - math.exp(-x/(R*C))) - 0.9*Q

def df(x):
    return math.exp(-x/(R*C))*(Q/(R*C))

def main():
    x0 = 0.5
    xk = x0 - f(x0)/df(x0)
    e = 0.0001
    er = abs(xk - x0)
    while er > e:
         x0 = xk
         xk = x0 - f(x0)/df(x0)
         er = abs(xk - x0)

    print(xk)

main()