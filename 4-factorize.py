def factorize(number):
    factors = []
    divisor = 2
    
     
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1 #  devisor increment
    
    # returns a value after iteration
    
    return factors

# Allow a user to enter any number so as to find its prime factors

number = int(input("Enter any number to find its prime factors: "))
prime_factors = factorize(number)
print(f"Prime factors of {number}: {prime_factors}")
