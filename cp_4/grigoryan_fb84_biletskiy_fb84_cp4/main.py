import random
import math
import requests
import json

def NSD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        nsd, x, y = NSD(b % a, a)
        return (nsd, y - (b // a) * x, x)

def obratnoe(b, n):
    nsd, x, y = NSD(b, n)
    if nsd == 1:
        return x % n


def primenumber_check(n, k):  # Міллер-Рабін
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    if n == 2 or n == 3:
        return True
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def GenerateKeyPair(n):
    while True:
        pair1 = []
        pair2 = []
        i = 0
        j = 0
        while i != 2:
            c = random.getrandbits(n)
            if not primenumber_check(c, 10):
                back = False
                while back is False:
                    c = random.getrandbits(n)
                    if primenumber_check(c, 10):
                        pair1.append(c)
                        i += 1
                        back = True
        while j != 2:
            c = random.getrandbits(n)
            if not primenumber_check(c, 10):
                back = False
                while back is False:
                    c = random.getrandbits(n)
                    if primenumber_check(c, 10):
                        pair2.append(c)
                        j += 1
                        back = True

        a1 = pair1[0] * pair1[1]
        b1 = pair2[0] * pair2[1]

        if a1 <= b1:
            return pair1, pair2


def FindOpenKey(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            d = obratnoe(e, phi)
            print("n " + str(n))
            print("e " + str(e))
            print("d " + str(d))
            return n, e, d


def Encrypt(K, e, n):
    return pow(K, e, n)


def Decrypt(K, d, n):
    return pow(K, d, n)


def Sign(K, d, n):
    return pow(K, d, n)


def Verify(K, s, e, n):
    return pow(s, e, n) == K


def SendKey(K, n1, d1, n2, e2):
    print("------SENDED KEYS---------")
    K1 = Encrypt(K, e2, n2)
    print("K1 = {}".format(hex(K1)[2:]))
    S = Sign(K, d1, n1)
    print("S = {}".format(hex(S)[2:]))
    S1 = Encrypt(S, e2, n2)
    print("S1 = {}".format(hex(S1)[2:]))

    return K1, S1


def ReceiveKey(eK, S1, n1, e1, n2, d2):
    print("------RECIEVED KEYS---------")
    S = Decrypt(S1, d2, n2)
    K = Decrypt(eK, d2, n2)
    if Verify(K, S, e1, n1):
        print("S = {}".format(hex(S)[2:]))
        print("K = {}".format(hex(K)[2:]))
        return K, S

while True:
    a = input("1.Server / 2.Local?")
    if a == '2':
        print('\n'*100)
        pair1, pair2 = GenerateKeyPair(256)
        p, q, p1, q1 = pair1[0], pair1[1], pair2[0], pair2[1]

        n1, e1, d1 = FindOpenKey(p, q)  # A
        n2, e2, d2 = FindOpenKey(p1, q1)  # B

        Message = random.randint(0, n1)
        print("K: " + str(hex(Message)[2:]))
        print(d2)
        EncryptedMessage, EncryptedSignature = SendKey(Message, n1, d1, n2, e2)
        ReceiveKey(EncryptedMessage, EncryptedSignature, n1, e1, n2, d2)
        print("\n" * 3)

    if a == '1':
        print('\n'*100)
        print('\n'*100)
        pair1, pair2 = GenerateKeyPair(256)
        p, q = pair1[0], pair1[1]
        n1, e1, d1 = FindOpenKey(p, q)  # A
        a = requests.get('http://asymcryptwebservice.appspot.com/rsa/serverKey?keySize=512')
        cookie = a.cookies
        cookie_name = cookie.keys()[0]
        cookie_value = cookie.values()[0]
        a = json.loads(a.text)
        e2 = int(a['publicExponent'], 16)
        n2 = int(a['modulus'], 16)
        while n2 < n1:
            pair1, pair2 = GenerateKeyPair(256)
            n1, e1, d1 = FindOpenKey(p, q)  # A
        Message = random.randint(0, n1)
        print("K: " + str(hex(Message)[2:]))
        EncryptedMessage, EncryptedSignature = SendKey(Message, n1, d1, n2, e2)
        cookie = {cookie_name:cookie_value}

        print("------RECIEVED KEYS---------")
        request = "http://asymcryptwebservice.appspot.com/rsa/receiveKey?key={k}&signature={s}&modulus={n}&publicExponent={e}".format(k=hex(EncryptedMessage)[2:],s=hex(EncryptedSignature)[2:],n=hex(n1)[2:],e=hex(e1)[2:])
        a = json.loads(requests.get(request,cookies=cookie).text)

        if a['key'][0] == '0':
            print("K: " + a['key'][1:])
        else: print("K: " + a['key'])
        print("Verified: " + str(a['verified']))
        print("\n"*3)