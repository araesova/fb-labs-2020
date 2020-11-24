import random
import math


def ensd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        nsd, x, y = ensd(b % a, a)
        return (nsd, y - (b // a) * x, x)


def reverse(b, n):
    nsd, x, y = ensd(b, n)
    if nsd == 1:
        return x % n


def primenumber_check(n, k):  # Міллер-Рабін
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
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
        num = random.randint(2, phi - 1)
        if math.gcd(num, phi) == 1:
            e = num
            return n, e, phi


pair1, pair2 = GenerateKeyPair(256)
p, q, p1, q1 = pair1[0], pair1[1], pair2[0], pair2[1]

n1, e1, phi1 = FindOpenKey(p, q)    # A
n2, e2, phi2 = FindOpenKey(p1, q1)  # B

d1 = reverse(phi1, e1)  # A:d
d2 = reverse(phi2, e2)  # B:d
print("A: " + str(d1), "B: " + str(d2), sep='\n')
