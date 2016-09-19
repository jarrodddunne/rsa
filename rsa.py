import random
import math
import datetime

def extendedEuclid(a,b):
    if a == 0:
        return (b,0,1)
    else:
        g,y,x = extendedEuclid(b%a,a)
        return (g,x-(b//a)*y,y)

def isPrime(n,acc):
    d = n
    s = 0
    while(d % 2 == 0):
        d /= 2
        s+=1
    for i in range (acc):
        a = random.randrange(2,n-1)
        x = (a**d) % n
        for r in range (s-1):
            cond1 = (a**d % n == 1)
            cond2 = (a**(2*r*d) % n == -1)
            if((cond1 or cond2) == False):
                return False
    return True

def largeRandPrime(bits):
    randnum = random.randrange(int(2**(bits-1)),int(2**bits))
    times = 0
    while not fermatsTheorem(randnum,100):
        times += 1
        randnum = random.randrange(2**(bits-1),2**bits)
    return randnum

def modularExponentiation(base, exp, mod):
    if exp < 1:
        return 1
    z = modularExponentiation(base, int(exp/2), mod)
    if exp % 2 == 0:
        return z**2 % mod
    else:
        return base * z**2 % mod

def fermatsTheorem(possible_prime, tests):
    if possible_prime % 2 == 0:
        return False
    for i in range(tests):
        randnum = random.randrange(1,possible_prime)
        modexp = modularExponentiation(randnum,(possible_prime-1),possible_prime)
        if modexp != 1:
            return False
    return True

def isPrimeLong(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def generateKeys(bits):
    prime1 = largeRandPrime(bits)
    prime2 = largeRandPrime(bits)
    pubkey1 = prime1*prime2
    pubkey2 = 3
    totient = (prime1-1) * (prime2 - 1)
    privatekey = extendedEuclid(pubkey2,totient)[2]
    return [pubkey1,pubkey2],privatekey

def encryptMessage(message, pubkey):
    encryptedMessage = modularExponentiation(message,pubkey[1],pubkey[0])
    return encryptedMessage

def decryptMessage(encryptedMessage, privatekey, pubkey):
    decryptedMessage = modularExponentiation(encryptedMessage,privatekey,pubkey[0])
    return decryptedMessage

def randNum(bits):
    return random.randrange(int(2**(bits-1)),int(2**bits))

def encryptionCycleTime(bits):
    begin = datetime.datetime.now()
    pubkey, privatekey = generateKeys(bits)
    message = randNum(bits-1)
    encryptedMessage = encryptMessage(message,pubkey)
    decrptedMessage = decryptMessage(encryptedMessage, privatekey, pubkey)
    end = datetime.datetime.now()
    return end - begin

for i in range(10,1000):
    print(i,encryptionCycleTime(i))
