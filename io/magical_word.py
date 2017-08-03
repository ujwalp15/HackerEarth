n = int(raw_input())

def check_prime(a):
   for i in range(2, a):
      if a % i == 0:
         return False
   return True

def find_nearest_prime(n):
    if n <= 65:
        return 67
    if n >= 122:
        return 113
    if check_prime(n):
        return n
    low = n - 1
    high = n + 1
    while True:
       if check_prime(low):
          return low
       elif check_prime(high):
          return high
       else:
          if low-1 >= 65:
              low -= 1
          if high-1 <=122:
              high += 1

for i in range(n):
    l = int(raw_input())
    s = raw_input()
    asc = [ord(i) for i in s]
    nearest_primes = [find_nearest_prime(i) for i in asc]
    asc = [chr(i) for i in nearest_primes]
    print (''.join(asc))
