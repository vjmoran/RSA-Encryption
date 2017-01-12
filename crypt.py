from random import *
from math import *

def main():
    while True:
        eOrD = str(input("Are you trying to encrypt or decrypt a message? "))
        if eOrD == "encrypt" or eOrD == "decrypt":
            break
        else:
            print("Please enter the word 'encrypt' or the word 'decrypt'")
    if eOrD == "encrypt":
        secret = str(input("What is the message you would like to have encrypted? "))
        while True:
            size = input("What is the approximate size you would like for your desired key? ")
            try:
                size = int(size)
                break
            except:
                print("Please enter a number.")
        key = chooseKey(size)
        # print("Your public key includes the encrpytion exponent, " + str(key[1]) + " and the modulus, " + str(key[2]) + ".")
        encrypted = encrypt(secret, (key[1], key[2]))
        print("The encrypted version of your message is " + str(encrypted) + ".")
        print("Your private key includes the decryption exponent, " + str(key[0]) + " and the modulus, " + str(key[2]) + ".")
        print("Now anyone with the encrypted message and private key can run this file to decrypt the message.")
    else:
        while True:
            encMessage = input("What is your encrypted message? ")
            try:
                if encMessage[0] == '[':
                    numbers = encMessage[1:-1].split()
                    encMessage = [int(x[:-1]) for x in numbers]
                else:
                    encMessage = [int(x[:-1]) for x in encMessage.split()]
                break
            except:
                print("The encrypted message should be a list.")
        while True:
            decEx = input("What is the decryption exponent? ")
            try:
                decEx = int(decEx)
                break
            except:
                print("The decryption exponent should be a number.")
        while True:
            mod = input("What is the modulus? ")
            try:
                mod = int(mod)
                break
            except:
                print("The modulus should be a number.")
        decrypted = decrypt(encMessage, (decEx, mod))
        print("The decrypted message is ''" + str(decrypted) + "'.")
                

def modularMultiplicativeInverse(n, m):
    """Compute the multiplicative inverse of n, modulo m.  Works only if
       n and m are relatively prime."""
    x, lastx = 0, 1
    y, lasty = 1, 0
    a = n
    b = m
    while b != 0:
        quotient = int(a / b)
        a, b = b, a % b
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    if lastx < 0:
	    lastx += m
    return lastx

def isPrime(n):
    """checks if n is prime"""
    for i in range(n):
        if i > 1:
            if n % i == 0:
                return False
    return True

def nextPrime(n):
    """finds the next prime number greater than n"""
    if n % 2 == 0:
        n -= 1
    while True:
        if isPrime(n + 2) == True:
            return n + 2
        n += 2

def gcd(a, b):
    """finds the greatest common denominator of a and b"""
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(b, a)

def chooseKey(n):
    """returns a decryption exponent, an encryption exponent, and a modulus"""
    p = randint(int(sqrt(n)/2), int(3*sqrt(n)/2))
    while isPrime(p) == False:
        p = randint(int(sqrt(n)/2), int(3*sqrt(n)/2))
    q = randint(int(sqrt(n)/2), int(3*sqrt(n)/2))
    while isPrime(q) == False:
        q = randint(int(sqrt(n)/2), int(3*sqrt(n)/2))
    if p == q:
        q = nextPrime(q)
    m = p * q
    totient = (p - 1) * (q - 1)
    e = randint(1, totient)
    while gcd(e, totient) != 1:
        e = randint(1, totient)
    d = modularMultiplicativeInverse(e, totient)
    return (d, e, m)

def encrypt(message, key):
    """returns a list of integers that represented the encrypted message"""
    L = []
    for i in message:
        secretNum = ord(i) ** key[0] % key[1]
        L += [secretNum]
    return L

def decrypt(L, key):
    """returns the decrypted message"""
    message = ""
    for i in range(len(L)):
        secretLett = chr(L[i] ** key[0] % key[1])
        message += secretLett
    return message

if __name__ == "__main__":
    main()