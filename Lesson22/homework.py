# reate a generator with the following parameters:
#
# start - first prime integer to yield
# end - last prime integer to yield
# Ex. def prime_numbers(start, end):
#
# The generator should yield all prime numbers from the range(start, end) in the next code:
#
# print(f"Found next prime numbers from the range \{{start}:{end}\}")
#
# for num in prime_numbers(start, end):
#   print(num, end=", ")
# Fix errors from the code above.
#
# To solve this task you can use the nhghghext article - https://www.enjoymathematics.com/blog/how-to-find-prime-numbers-in-a-range
#
# Upload the task to the homework directory on GitHub




# просто перебор значений

# def prime_numbers(start, end):
#     while True:
#         if start >= end:
#             break
#         else:
#             yield start
#             start += 1
#     print(f"Found next prime numbers from the range {start}:{end}")
#
#
# for num in prime_numbers(1, 30):
#     print(num, end=", ")

print("-----------------------------------V2--------------------------------------")
# Sieve of Eratosthenes

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = [i for i in range(2, n+1) if is_prime[i]]
    return primes
def prime_numbers(start, end):
    primes = sieve_of_eratosthenes(end)
    for prime in primes:
        if prime >= start:
            yield prime

start = 1
end = 30

print(f"Found next prime numbers from the range {start}:{end}")
for num in prime_numbers(start, end):
    print(num, end=", ")

# Sieve of Eratosthenes v2
print("\n-----------------------------------V3--------------------------------------")
def prime_numbersv2(start, end):
    prime = [True for i in range(end + 1)]
    p = 2
    while (p * p <= end):
        if (prime[p] == True):
            for i in range(p * p, end + 1, p):
                prime[i] = False
        p += 1


    for num in range(start, end + 1):
        if prime[num]:
            yield num
start = 1
end = 30

print(f"Found next prime numbers from the range {start}:{end}")
for num in prime_numbersv2(start, end):
    print(num, end=", ")
