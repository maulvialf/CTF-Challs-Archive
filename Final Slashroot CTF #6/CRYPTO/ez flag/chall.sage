from secret import flag

p = random_prime(1 << 1024)
q = random_prime(1 << 1024)
n = p * q

print("n =", n)

x = int.from_bytes(flag, "big")
y = randint(0, n-1)

a = randint(0, n-1)
b = (y^2 - (x^3 + a*x)) % n

EC = EllipticCurve(Zmod(n), [a, b])

P = EC((x, y))
Q = 2 * P

print("a, b =", [a, b])
print("Q =", Q.xy())

m = int.from_bytes(flag, "big")
t = randint(0, n-1)

c = power_mod(m + t, 65537, n)
print("t =", t)
print("c =", c)