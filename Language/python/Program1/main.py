# Python program to print prime numbers in an interval


def print_primes(lower_limit: int, upper_limit: int) -> None:
    while lower_limit < upper_limit + 1:
        if lower_limit > 1:
            interval = 2
            while interval < lower_limit:
                if lower_limit % interval == 0:
                    break
                interval += 1
            else:
                print(lower_limit)

        lower_limit += 1

        
def print_primes_with_for(lower_limit: int, upper_limit: int) -> None:
    for i in range(lower_limit, upper_limit + 1):
        if i > 1:
            interval = 2
            for k in range(interval, i):
                if i % k == 0:
                    break
            else:
                print(i)

# Taking inputs

lower = int(input("Lower Limit: "))
upper = int(input("Upper Limit: "))

print_primes_with_for(lower, upper)
