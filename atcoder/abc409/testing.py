mod = 998244353

import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    P_val = int(data[1])
    p_val = P_val
    if n > 5000:
        for k in range(1, n+1):
            print(0)
        return

    p = (p_val * pow(100, mod-2, mod)) % mod
    q = (1 - p) % mod

    max_i = n-1

    inv = [0] * (max_i+2)
    inv[1] = 1
    for i in range(2, max_i+2):
        inv[i] = (mod - (mod // i) * inv[mod % i] % mod) % mod

    max_n = max_i
    fact = [1] * (max_n+1)
    inv_fact = [1] * (max_n+1)
    for i in range(1, max_n+1):
        fact[i] = fact[i-1] * i % mod
    inv_fact[max_n] = pow(fact[max_n], mod-2, mod)
    for i in range(max_n, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % mod

    power_p = [1] * (max_i+1)
    power_q = [1] * (max_i+1)
    for i in range(1, max_i+1):
        power_p[i] = power_p[i-1] * p % mod
        power_q[i] = power_q[i-1] * q % mod

    dp = []
    cum = []
    for i in range(0, max_i+1):
        arr = [0] * (i+1)
        for j in range(0, i+1):
            comb = fact[i] * inv_fact[j] % mod * inv_fact[i-j] % mod
            arr[j] = comb * power_p[j] % mod * power_q[i-j] % mod
        dp.append(arr)
        cum_arr = [0] * (i+1)
        cum_arr[i] = arr[i]
        for j in range(i-1, -1, -1):
            cum_arr[j] = (cum_arr[j+1] + arr[j]) % mod
        cum.append(cum_arr)

    res = [0] * (n+1)

    g1 = 1
    for i in range(0, n-1):
        numerator = ( (i+1) + (1 - p) ) % mod
        g1 = g1 * numerator % mod * inv[i+1] % mod
    res[1] = g1

    for k in range(2, n+1):
        g = 0
        for i in range(0, n-1):
            a_val = 0
            if i >= k-1:
                a_val = cum[i][k-1]
            else:
                a_val = 0
            term1 = 0
            if k-2 >= 0 and k-2 <= i:
                term1 = p * dp[i][k-2] % mod
            else:
                term1 = 0
            term2 = (1 - p) % mod * g % mod * a_val % mod * inv[i+1] % mod
            g = (g + term1 + term2) % mod
        res[k] = g

    for k in range(1, n+1):
        print(res[k])

if __name__ == '__main__':
    main()