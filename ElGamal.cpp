#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
//ham luy thua modulo nhanh
long long modpow(long long a, long long b, long long n) {
    long long result = 1;
    a %= n;
    while (b > 0) {
        if (b % 2 == 1)
            result = (result * a) % n;
        a = (a * a) % n;
        b /= 2;
    }
    return result;
}
//kiem tra q có phai snt khong
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i*i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}

int main() {
    //tao tinh ngau nhien
    srand(time(0));
    cout << "=== ElGamal Algorithm ===" << endl;
//sinh khoa
    int q, g;
    do {
        cout << "Nhập số nguyên tố q: ";
        cin >> q;
    } while (!isPrime(q));

    do {
        cout << "Nhập số nguyên g (1 < g < " << q << "): ";
        cin >> g;
    } while (g <= 1 || g >= q);

    int x = rand() % (q - 2) + 1; // bí mật x từ 1 đến q-2
    int h = modpow(g, x, q);
    cout << "Public key (q, g, h): (" << q << ", " << g << ", " << h << ")\n";
    cout << "Private key x: " << x << endl;
//ma hoa
    int m;
    do {
        cout << "Nhập thông điệp m (0 <= m < " << q << "): ";
        cin >> m;
    } while (m < 0 || m >= q);

    int k = rand() % (q - 2) + 1;
//tinh ciphertext    
    int p = modpow(g, k, q);
    int s = modpow(h, k, q);
    int c = (s * m) % q;

    cout << "Ciphertext: (" << p << ", " << c << ")\n";
//giai ma, s_inv la nghich dao s, Fetmat nho
    int s_inv = modpow(p, q - 1 - x, q);  
    int decrypted = (c * s_inv) % q;
    cout << "Bản rõ sau khi giải mã: " << decrypted << endl;

    return 0;
}
