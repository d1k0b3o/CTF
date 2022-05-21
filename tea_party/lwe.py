import numpy as np
import random
from Crypto.Util.number import long_to_bytes, bytes_to_long

def randint_from_gaussian(alpha,size):
    sigma = alpha / np.sqrt(2*np.pi)
    x = np.random.normal(0,sigma,size)
    return np.rint(x)

def KeyGen(params):
    a,n,q = params
    A = np.random.randint(q, size=(n,n))
    s = np.random.randint(q, size=n)
    e = randint_from_gaussian(a,size=n)
    B = (np.dot(A,s)+e)%q
    pk = (A,B)
    sk = s
    return pk,sk

def Enc(m,pk,params):
    a,n,q = params
    A,B = pk
    r = randint_from_gaussian(a, size=n)
    u = np.dot(r,A)%q
    v = (np.dot(r,B) - round(q/2)*m )%q
    return (u,v)

def Dec(c,sk,params):
    a,n,q = params
    u,v = c
    s = sk
    m = (np.dot(u,s)-v)%q
    if round(q/4) < m and m < 3*round(q/4): return 1
    else: return 0

if __name__ == '__main__':
    a = 8.0
    n = 50
    q = 1021
    params = (a,n,q)

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

    print('*** Smaaall LWE cryptography ***\n')
    print('=== Parameters ===')
    print('n :',n)
    print('q :',q)
    print()
    print('=== Message ===')
    print('m (bytes)   :',mb)
    print('m (integer) :',m)
    print('m (binary)  :',bin(m)[2:])
    print('(',len(bin(m))-2,'bit )')
    print()
    print('=== KeyGen ===')
    print('[+] pk(A,B)')
    print('A :')
    print(pk[0])
    print('B :')
    print(pk[1])
    print()
    print('[+] sk(s)')
    print('s :')
    print(sk)
    print()
    print('=== Enc ===')
    print('[+] Cipher')
    print(C)
    print()
    print('=== Dec ===')
    print('[+] Decrypted')
    print(ans)
    print(long_to_bytes(ans))
