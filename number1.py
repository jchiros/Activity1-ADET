# Accept a positive value. Output all the factors of the input. Determine also if the number
# is a PRIME number or COMPOSITE number.

def prime_checker(number):
    isPrime = True
    for num in range(2, number):
        if number % num == 0:
            isPrime = False
    if isPrime:
        factors(n)
        print("\nPrime Number")
    else:
        factors(n)
        print("\nComposite Number")

def factors(num):
    print("Factors: ", end= " ")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=", ")


n = int(input("Enter a positive value: "))
if n < 0:
    print("Invalid Input")
else:
    prime_checker(n)