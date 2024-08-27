import math
def find_prime(n):
    count = 0
    num_count = 2
    while count < n:
        if (math.factorial(num_count - 1) + 1)%num_count == 0:
            count += 1
            if count == n:
                break
        num_count += 1
    print(num_count)
find_prime(100)