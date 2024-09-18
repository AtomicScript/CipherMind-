'''
RSA Encryption and Decryption

Objective:
Implement RSA encryption and decryption in Python.

Tasks:

Generate two large prime numbers.
Compute n and Euler's totient function φ(n).
Choose an encryption key e and calculate the decryption key d.
Write functions to encrypt and decrypt a message.

Bonus: Add message padding (e.g., PKCS#1 v1.5 padding).


https://www.youtube.com/watch?v=D_PfV_IcUdA

'''

import random
import math

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, (number // 2) + 1):
        if number % i == 0 :
            return False
    
    return True


def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
        
    raise ValueError("[!] mod_inverse does not exists")


## RSA Requires large prime numbers to start the encryption 
p,q = generate_prime(1000,5000), generate_prime(1000,5000)

while p == q:
    q = generate_prime(1000,5000)


# Compute n
n = p * q

# Compute Euler's totient function φ(n).
phin = (p - 1) * (q - 1)

print(f"p = {p}, q = {q}")
print(f"n = {n}, φ(n) = {phin}")

# public key
e = random.randint(3, phin-1)
print(f"Encryption key (e): {e}")


# has to be coprime
while math.gcd(e, phin) != 1:
    e = random.randint(3, phin-1)

# private key 
d = mod_inverse(e, phin)
print(f"Decryption key (d): {d}")

message = 'Hello World!'


# ascii char
message_encoded = [ord(ch) for ch in message]
#(m ^ e) mod n
ciphertext = [pow(ch, e, n) for ch in message_encoded]



message_encoded = [pow(ch, d, n) for ch in ciphertext]
decrypted_message = "".join(chr(ch) for ch in message_encoded)

print(f"Message integer: {message_encoded}")
print(f"Ciphertext integer: {ciphertext}")
print(f"Decrypted integer: {decrypted_message}")










