'''
# LWE Cryptography proposed by Peikert

: Chris Peikert, "Public-Key Cryptosystems from the Worst-Case Shortest Vector Problem"

'''
import numpy as np
import random
import math
from Crypto.Util.number import bytes_to_long,long_to_bytes,getPrime

def from_gaussian(alpha,size):
    sigma = alpha/np.sqrt(2*np.pi)
    x = np.random.normal(0,sigma,size)
    return np.rint(x)

def KeyGen(params):
    n,m,l,q,a = params
    A = np.random.randint(q,size=(n,m))
    X = np.random.randint(2,size=(m,l))
    U = np.dot(A,X)
    return (A,U),X

def Enc(g,pk,params):
    n,m,l,q,a = params
    A,U = pk
    s = np.random.randint(q,size=n)
    e1 = from_gaussian(a,size=m)
    e2 = from_gaussian(a,size=l)

    b1 = np.dot(A.T,s)/q + e1
    b2 = np.dot(U.T,s)/q + e2 + g/2

    for i in range(m): b1[i] = round(q*b1[i])
    for j in range(l): b2[j] = round(q*b2[j])
        
    return (b1%q,b2%q)

def Dec(c,sk,params):
    n,m,l,q,a = params
    b1,b2 = c
    X = sk
    h = (b2 - np.dot(X.T,b1))%q
    g = np.zeros(l,dtype=int)
    for i in range(l):
        if -math.floor(q/2) < h[i] < math.floor(q/2): g[i] = 0
        else:                                         g[i] = 1
    return g


if __name__ == '__main__':
    n,m,l,q,a = 10,16,16,73,8.0
    params = (n,m,l,q,a)
    pk,sk = KeyGen(params)

    g = np.random.randint(2,size=l)
    c = Enc(g,pk,params)
    b1,b2 = c
    gg = Dec(c,sk,params)
    print('cipher')
    print('b1')
    print(b1)
    print('b2')
    print(b2)
    print('message  :',g)
    print('decrypted:',gg)
