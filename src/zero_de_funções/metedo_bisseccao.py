import numpy as np

def met_bissec_erro(fun, a, b, erro):
    if fun(a)*fun(b)>0:
        print("não tem raiz nesse intervalo")
        return -1
    else:
        n = int(np.log2(abs(b-a)/erro))
        xn = (a+b)/2
        for i in range(n):
            if (fun(a)*fun(xn)<0):
                b = xn
                xn = (xn+a)/2
            elif (fun(b)*fun(xn)<0):
                a = xn
                xn = (xn+b)/2
        return xn

def met_bissec_n(fun, a, b, n):
    if fun(a)*fun(b)>0:
        print("não tem raiz nesse intervalo")
        return -1
    else:
        xn = (a+b)/2
        for i in range(n-1):
            if (fun(a)*fun(xn)<0):
                b = xn
                xn = (xn+a)/2
            elif (fun(b)*fun(xn)<0):
                a = xn
                xn = (xn+b)/2
        return xn

#exemple_1
e = 2.7183
g = lambda x : (33*x*e**(-0.2*x) - 25)
res = met_bissec_erro(g,10,20,1/60)
print(res)
