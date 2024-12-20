def prime_check(n):
    if n==0 or n==1 :
        return False #returns false as 0 and 1 are not prime
    elif n==2:
        return True #retrurns True as 2 is prime
    else:
        for i in range(2,n):
            if n%i==0:#return false if n is divisible by other number than 1 and itself
                return False
       
        return True #return true if its not divisible by any other number other than 1 and itself (it means its a prime number)

prime=[]
#let's check for numbers till 999
for i in range(0,1000):
    if prime_check(i)==True:
        prime.append(i)

print("prime: ")
print(prime) #this will print all the prime numbers from 2 to 999





