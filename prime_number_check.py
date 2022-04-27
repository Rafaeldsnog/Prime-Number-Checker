import math

def prime_checker(number):
    for ii in range(2,math.ceil(number)):
        if number%ii==0:
            print(f"The number {number} is not prime.")
            return
        else:
            pass
    print(f"The number {number} is prime.")

number = int(input("Check this number: "))
prime_checker(number)
