# TO WRITE THE DIVISOR OR THE GIVEN NUMBERS IN PYTHON

def divi(*nums):
    for num in nums:
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        print(f"Divisors of {num}: {divisors}")

divi(10, 20, 30)





















# repo created by kerston2104