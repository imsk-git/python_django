
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
        else:
            return True
        
input_number = int(input("Enter number: "))
isPrime_output = isPrime(input_number)

if isPrime_output == True:
    print("It's Prime number.")
else:
    print("It's Composite number.")