def primes(kmax):
    def n,k,i
    def p[1000]
    result = []
    if kmax > 1000:
        kmax = 1000
    k = 0
    n = 2
    while k < kmax:
        i = 0
        # p[i]里面放的素数
        # n不能被p[i]整除，看看i == k，如果相等，证明直到找到第k-1个素数，都找不到可以整除n的素数
        # 则n为第k个素数
        # n不能被小于他的所有素数整除
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
        n = n + 1
    return result