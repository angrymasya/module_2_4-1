numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = 'не добавлять'
    for j in range(2,i):
        if i%j == 0:
            is_prime = 'добавлять'
    #print(is_prime)
    if is_prime == 'добавлять':
        not_primes.append(i)
    else :
        primes.append(i)
print(primes)
print(not_primes)
