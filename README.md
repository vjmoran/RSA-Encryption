# RSA Encryption

**Running the File**

Download and unzip the RSA-Encryption.zip file. Open Terminal and run the following commands:

*ipython*

*cd Downloads*

*cd RSA-Encryption*

*run crypt.py*

**The Idea**

The RSA method is based on modular exponentiation—i.e., taking a number to a power modulo some other number. 

For example, you might encrypt the message M by raising it to the power of 23, modulo 143. The encrypted message would therefore be M^23 % 143. If M = 7, then 7^23 % 143 = 2. Then we can decrypt it by raising 2 to the 47th power modulo 143, which equals 7.

This program chooses a key with three numbers: a decryption exponent d, an encryption exponent e, and a modulus m. The encryption exponent and the modulus will be published as the public key; the decryption exponent and the modulus will be your private key.

**Disclaimer**

This encryption implementation is not industrial strength. Anyone can use a brute force algorithm to decrypt the message, which is escpecially practical for relatively small keys. Also, this is monoalphabetic cipher and can be easily broken through frequency analysis.
