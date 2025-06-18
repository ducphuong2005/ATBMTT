import random
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def modinv(a, m):
    # Tính nghịch đảo modulo
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Nghịch đảo không tồn tại')
    return x % m

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extended_gcd(b, a % b)
    return g, x, y - (a // b) * x

def elgamal_keygen():
    while True:
        q = int(input("Nhập số nguyên tố q (prime modulus): "))
        if is_prime(q):
            break
        print("q không phải là số nguyên tố. Nhập lại!")

    while True:
        g = int(input(f"Nhập số nguyên g (1 < g < {q}): "))
        if 1 < g < q:
            break
        print("g không hợp lệ. Nhập lại!")

    x = random.randint(1, q-2)  # private key
    h = pow(g, x, q)  # public h

    print(f"Public key (q, g, h): ({q}, {g}, {h})")
    print(f"Private key x: {x}")
    return q, g, h, x

def elgamal_encrypt(m, q, g, h):
    if not (0 <= m < q):
        raise ValueError(f"Thông điệp m phải nằm trong khoảng [0, {q-1}]")
    y = random.randint(1, q-2)
    p = pow(g, y, q)
    s = pow(h, y, q)
    c = (s * m) % q
    return (p, c)

def elgamal_decrypt(p, c, q, x):
    s = pow(p, x, q)
    s_inv = modinv(s, q)
    m = (c * s_inv) % q
    return m

# Chạy thử
q, g, h, x = elgamal_keygen()
m = int(input(f"Nhập thông điệp (số nguyên 0 <= m < {q}): "))
ciphertext = elgamal_encrypt(m, q, g, h)
print(f"Bản mã sau khi mã hóa là: {ciphertext}")


decrypted = elgamal_decrypt(ciphertext[0], ciphertext[1], q, x)
print("Bản rõ sau khi giải mã:", decrypted)
