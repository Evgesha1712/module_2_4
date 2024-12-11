numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range(len(numbers)):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            primes.append(i)
            for j in range(2, i):
                if (i % j) != 0:
                    break
            else:
                not_primes.append(i)


print('primes: ', primes)
print('not_primes: ', not_primes)