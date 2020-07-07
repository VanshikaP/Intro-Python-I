import sys
import math

def isPrime():

    if len(sys.argv) < 2 or (not str.isnumeric(sys.argv[1])):
        print('Correct Usage: prime.py [number]')
        return None
    else:
        n = int(sys.argv[1])
        print(n)
        if n < 2:
            print('Enter a number greater than 1')
            return None
        else:
            numbers = [x+2 for x in range(n-1)]
            prevPrimeIndex = -1
            # outer loop - iterate through prime numbers
            for i in range(int(math.sqrt(n))):
                # get the prime number for this iteration
                for j in range(prevPrimeIndex+1, int(math.sqrt(n))):
                    if numbers[j] != 0:
                        currPrime = numbers[j]
                        break
                if i != 0 and currPrime == numbers[prevPrimeIndex]:
                    break
                else:
                    prevPrimeIndex = j
                    # sieve the numbers in increments of currPrime
                    for k in range(j+currPrime, n-1, currPrime):
                        if numbers[k] != 0:
                            numbers[k] = 0
                    
            # check if the number is crossed or not
            if numbers[n-2] == 0:
                print('Not Prime.')
            else:
                print('Prime!')

isPrime()
            
            
            

