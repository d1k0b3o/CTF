'''
# LWE Cryptography proposed by Regev

: Oded Regev, "On Ideal Lattices, Learning with Errors, Random Linear Codes, and Cryptography"

結構な確率で失敗する。
'''
import numpy as np
import math
import random
from Crypto.Util.number import long_to_bytes,bytes_to_long

def from_gaussian(alpha,size):
    sigma = alpha/np.sqrt(2*np.pi)
    x = np.random.normal(0,sigma,size)
    return np.rint(x)

def KeyGen(params):
    n,m,p = params
    # Secret Key
    s = np.random.randint(p,size=n)         # from uniform distribution
    # Private Key
    a = np.random.randint(p, size=(m,n))    # from uniform distribution
    e = from_gaussian(2, size = m)        # from gaussian distribution
    print('e',e)
    b = (np.dot(a,s) + e)%p

    return (a,b),s

def Enc(m_bit,pk,params):
    n,m,p = params
    a,b = pk
    A = np.zeros(n,dtype=int)
    B = 0
    for i in range(m):
        A += a[i]
        B += b[i]
    if m_bit == 0:
        return (A%p,B%p)
    else:
        return (A%p,(B+math.floor(p/2))%p)

def Dec(c,sk,params):
    n,m,p = params
    a,b = c
    s = sk
    res = (b - np.dot(a,s))%p
    if res < math.floor(p/2): return 0
    else : return 1
    

if __name__ == '__main__':
    n,m,p = 100,120,1021
    params = (n,m,p)

    # 平文
    mb = b'kurenaif'
    m = bytes_to_long(mb)

    # 鍵生成
    pk,sk = KeyGen(params)

    # 1bitずつ暗号化
    C = list()
    i = pow(2,m.bit_length()-1)
    while i > 1:
        if m&i > 0: c = Enc(1,pk,params)
        else:       c = Enc(0,pk,params)
        C.append(c)
        i >>= 1

    # 復号
    ans = 0
    for cc in C:
        mi = Dec(cc,sk,params)
        ans += mi
        ans <<= 1

    print('m',m)
    print(bin(m))

    print('ans',ans)
    print(bin(ans))

    print('=== message ===')
    print('m (bytes)',mb)
    print('=== decrypted ===')
    print('mm (bytes)',long_to_bytes(ans))

