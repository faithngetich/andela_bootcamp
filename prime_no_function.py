def number(num):
   return num

def prime(n):
   if_prime = True
   # since 2, 0 or negative numbers are not  prime numbers, we use it
   x = 2
   if n == 0 or n < 0:
       return False
   else:
       for i in range(2,n):
            #checks if the remainder of number(n) divided current iteration value gives zero
           if n % i == 0:
               # in a case  result is Zero(0), means n is divisible by another value apart from itsself and 1
               if_prime = False
   # the value status returns tells if number is prime=True or not=False
   return if_prime

def array_of_prime_integers(n):
   # has an array/list of prime numbers
   array_of_prime_numbers = []
   for i in range(0, n):
       if prime_number(i):# if True append to list
           array_of_prime_numbers.append(i)
   return array_of_prime_numbers 

