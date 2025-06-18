def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def power(base, expo, mod):
    res = 1
    base = base % mod
    while expo > 0:
        if expo & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        expo //= 2
    return res

# Sinh khóa RSA
def generate_keys():
    # Nhập p
    while True:
        try:
            p = int(input("Nhập số nguyên tố p: "))
            if is_prime(p):
                break
            else:
                print("p không phải số nguyên tố. Nhập lại!")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    # Nhập q
    while True:
        try:
            q = int(input("Nhập số nguyên tố q: "))
            if is_prime(q) and q != p:
                break
            else:
                print("q phải là số nguyên tố khác p. Nhập lại!")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Nhập e
    while True:
        try:
            e = int(input(f"Nhập e (1 < e < {phi}), thỏa mãn gcd(e, {phi}) = 1: "))
            if 1 < e < phi and gcd(e, phi) == 1:
                break
            else:
                print("e không hợp lệ. Nhập lại!")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    # Tính d
    d = mod_inverse(e, phi)
    if d == -1:
        raise ValueError("Không tìm được d hợp lệ!")

    return (e, n), (d, n)

# Mã hóa
def encrypt(m, pubkey):
    e, n = pubkey
    if m < 0 or m >= n:
        raise ValueError("Bản rõ (plaintext) phải nằm trong khoảng [0, n-1].")
    return power(m, e, n)

# Giải mã
def decrypt(c, privkey):
    d, n = privkey
    return power(c, d, n)

# Chương trình chính
if __name__ == "__main__":
    print("=== RSA Algorithm ===")
    public_key, private_key = generate_keys()
    e, n = public_key
    d, _ = private_key

    print(f"\nKhóa công khai (e, n): ({e}, {n})")
    print(f"Khóa bí mật (d, n): ({d}, {n})")

    while True:
        try:
            m = int(input(f"\nNhập thông điệp (số nguyên 0 <= m < {n}): "))
            if 0 <= m < n:
                break
            else:
                print("Thông điệp không hợp lệ. Nhập lại!")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    c = encrypt(m, public_key)
    print(f"\nBản mã sau khi mã hóa: {c}")

    m_decrypted = decrypt(c, private_key)
    print(f"Bản rõ sau khi giải mã: {m_decrypted}")
