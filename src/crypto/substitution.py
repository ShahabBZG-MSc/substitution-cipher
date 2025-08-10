"""
Auto-generated from notebook: substitution_ciphers.ipynb
Exported on: 2025-08-10T18:39:10.035462Z
NOTE: This file is produced by concatenating code cells (magics removed).
"""

import string
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pickle
from crypto.paths import DATA_DIR

def caesar_encrypt(plaintext, shift=0):
    ''' Encrypt `plaintext` (str) as a caesar cipher with a given `shift` (int) 
    '''
    alphabet = list(string.ascii_lowercase)  # ['a', 'b', 'c', ..., 'z']
    ciphertext = []  # for store the modified text
    for letter in plaintext:
        if letter in alphabet:
            position = alphabet.index(letter)  # Get index (0-based)
            new_position = (position + shift) % 26  # shift alphabet
            ciphertext.append(alphabet[new_position]) # replace letter by new alphabet
        else:
            ciphertext.append(letter)  # Keep non-alphabet characters unchanged
    ciphertext = ''.join(ciphertext)  # Join list to string
    return ciphertext

# code snippet to test the implementation of the encryption function
plaintext = 'hello!' 
ciphertext = caesar_encrypt(plaintext, shift=4)

print(plaintext, '->', ciphertext) # expected output 'hello! -> lipps!'

def caesar_decrypt(ciphertext, shift=0):
    ''' Decrypt `ciphertext` (str) as a caesar cipher with a given `shift` (int) 
    '''
    alphabet = list(string.ascii_lowercase)  # ['a', 'b', 'c', ..., 'z']
    plaintext = []  # Store the modified text
    for letter in ciphertext:
        if letter in alphabet:
            position = alphabet.index(letter)  # Get index (0-based)
            new_position = (position - shift) % 26  # Ensure wrap-around
            plaintext.append(alphabet[new_position])
        else:
            plaintext.append(letter)  # Keep non-alphabet characters unchanged
    plaintext = ''.join(plaintext)  # Convert list to string

    return plaintext

# code snippet to test the implementation of the decryption function
ciphertext = 'lipps!' # 'hello!' encoded with shift=4
plaintext = caesar_decrypt(ciphertext, shift=4)

print(ciphertext, '->', plaintext)  # expected output 'lipps! -> hello!'

file_path = DATA_DIR / "ciphertext_caesar.txt"  # Input the Ciphertext file path
with open(file_path, "r", encoding="utf-8") as file:
    ciphertext = file.read().strip()    # Read the whole file and remove extra spaces

for shift in range(26):    #implement decryption algorithm for all shifts
    plaintext = caesar_decrypt(ciphertext, shift) 
    print('__________________________________________________________________')
    print(f"{shift} : {''.join(plaintext[:100])}")

shift = 18
plaintext = caesar_decrypt(ciphertext, shift) 
print(f"{shift} : {''.join(plaintext)}")

def substitution_encrypt(plaintext, mapping):
    ''' Encrypt `ciphertext` (str) as a simple substitution cipher with a given 
        `mapping` (??) from plaintext letters to ciphertext letters '''
		
    ciphertext = []		# Create an empty list to collect encrypted characters
    # Iterate over each character in the plaintext
    for char in plaintext:
        if char.isalpha():  # Check if the character is an alphabetic letter
            ciphertext.append(mapping[char])  # If it's a letter, substitute it using the mapping
        else:
            ciphertext.append(char)  # If it's not a letter (e.g., punctuation or space), keep it as is
    
    ciphertext = ''.join(ciphertext)  # Join the list of characters into a string to form the ciphertext
    return ciphertext  # Return the final encrypted string

# code snippet to test the implementation of the encryption function
plaintext = 'hello!'
mapping = {'h': 'a', 'e': 'p', 'l': 'w', 'o': 'q'} 

ciphertext = substitution_encrypt(plaintext, mapping)

print(plaintext, '->', ciphertext) # expected output 'hello! -> apwwq!'

def substitution_decrypt(ciphertext, mapping):
    ''' Decrypt `ciphertext` (str) as a simple substitution cipher with a given 
       `mapping` (dict) from plaintext letters to ciphertext letters '''
    
    inverse_mapping = {v: k for k, v in mapping.items()}  # Create an inverse mapping
    plaintext = []  # Create an empty list to collect decrypted characters
    
    for char in ciphertext:
        if char.isalpha() and char.isascii():
            plaintext.append(inverse_mapping[char])  # Append to the plaintext list
        else:
            plaintext.append(char)  # Append non-alphabet characters as is
    
    plaintext = ''.join(plaintext)  # Join the list into a string
    return plaintext

# code snippet to test the implementation of the decryption function
mapping = {'h': 'a', 'e': 'p', 'l': 'w', 'o': 'q'}  # previous mapping 
ciphertext = 'apwwq!'

plaintext = substitution_decrypt(ciphertext, mapping)

print(ciphertext, '->', plaintext)  # expected output 'apwwq! -> hello!'

# Load ciphertext
file_path = DATA_DIR / "ciphertext_simple.txt"
with open(file_path, "r", encoding="utf-8") as file:
    ctext = file.read()
    print(ctext)

# function to infer the letter distribution from a text
def letter_distribution(text):
    ''' Return the `distribution` (??) of the letters in `text` (str) '''
   
    filtered_txt = ''.join([char for char in text if char in string.ascii_lowercase])
    n = len(filtered_txt)
    distribution = Counter(filtered_txt)
    distribution = {char: count / n for char, count in sorted(distribution.items())}
    return distribution

# code snippet to test the implementation of `letter_distribution`
text = 'hello world!'

letter_distribution(text)
# expected ouput: 
# {'d': 0.1, 'e': 0.1, 'h': 0.1, 'l': 0.3, 'o': 0.2, 'r': 0.1, 'w': 0.1, ...}

# Load English Text
file_path = DATA_DIR / "wikipedia_cybersecurity.txt"
with open(file_path, "r", encoding="utf-8") as file:
    txt = file.read().lower()
    print(txt)

# estimate the English letters distribution 
txt_distribituin = letter_distribution(txt)
print(txt_distribituin)

# plot the English letter distribution
plt.bar(txt_distribituin.keys(), txt_distribituin.values(), align="center", width=0.5, alpha=0.5, color="red")
plt.title("Letter Frequency Distribution")
plt.xlabel("Letters")
plt.ylabel("Frequency")

# store the distribution as a pickle file
with open("eng_dst.pkl", "wb") as f:
    pickle.dump(txt_distribituin, f)

# perform Frequency analysis attack
ciphertext_distribiution = letter_distribution(ctext)
ciphertext_distribiution = {k: v for k, v in sorted(ciphertext_distribiution.items(), key=lambda x: x[1], reverse=True)}
txt_distribituin = {k: v for k, v in sorted(txt_distribituin.items(), key=lambda x: x[1], reverse=True)}
mapping = {txt_key: cipher_key for (txt_key, _), (cipher_key, _) in zip(txt_distribituin.items(), ciphertext_distribiution.items())}
fig , axes = plt.subplots(2, 1, figsize=(6, 12))
axes[0].bar(txt_distribituin.keys(), txt_distribituin.values(), align="center", width=0.5, alpha=0.5, color="blue")
axes[0].set_title("Eng Alphabet Letter Distribution")
axes[0].set_xlabel("Letters")
axes[0].set_ylabel("Frequency")
axes[1].bar(ciphertext_distribiution.keys(), ciphertext_distribiution.values(), align="center", width=0.5, alpha=0.5, color="red")
axes[1].set_title("Ciphertext Letter Distribution")
axes[1].set_xlabel("Letters")
axes[1].set_ylabel("Frequency")

# print mapping
print(mapping)

# print decrypted plaintext
plaintext = substitution_decrypt(ctext, mapping)
print(plaintext)

new_mapping = {'r' : 's', 'o' : 'd', 'w' : 'u', 'p' : 'y', 'c' : 'p'}

reverse_mapping = {v: k for k, v in mapping.items()}

for key, new_value in new_mapping.items():
    # Find the key that currently holds new_value
    old_key = reverse_mapping[new_value]

    # Swap values
    mapping[old_key], mapping[key] = mapping[key], new_value

    # Update reverse mapping
    reverse_mapping[mapping[old_key]] = old_key
    reverse_mapping[mapping[key]] = key
        

print(f'mapping: {mapping}\n')              
print(f'plaintext:\n {substitution_decrypt(ctext, mapping)}')

new_mapping = {'m' : 'k', 'y' : 'e', 'd' : 'j' , 'f' : 'r' , 'u' : 'x' , 'b' : 'o'}

reverse_mapping = {v: k for k, v in mapping.items()}

for key, new_value in new_mapping.items():
    # Find the key that currently holds new_value
    old_key = reverse_mapping[new_value]

    # Swap values
    mapping[old_key], mapping[key] = mapping[key], new_value

    # Update reverse mapping
    reverse_mapping[mapping[old_key]] = old_key
    reverse_mapping[mapping[key]] = key

print(f'mapping: {mapping}\n')
print(f'plaintext:\n {substitution_decrypt(ctext, mapping)}')

new_mapping = {'q' : 'h'}

reverse_mapping = {v: k for k, v in mapping.items()}

for key, new_value in new_mapping.items():
    # Find the key that currently holds new_value
    old_key = reverse_mapping[new_value]

    # Swap values
    mapping[old_key], mapping[key] = mapping[key], new_value

    # Update reverse mapping
    reverse_mapping[mapping[old_key]] = old_key
    reverse_mapping[mapping[key]] = key

print(f'mapping: {mapping}\n')
print(f'plaintext:\n {substitution_decrypt(ctext, mapping)}')

from math import gcd


def affine_encrypt(plaintext, a, b):
    ''' Encrypt `plaintext` (str) as an affine cipher with given `a` and `b` 
    '''
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
        ciphertext.append(char)
    ciphertext = ''.join(ciphertext)
    return ciphertext

plaintext = 'hello world!'
a, b = 3, 1

ciphertext = affine_encrypt(plaintext, a, b)
print(plaintext, '->', ciphertext) # expected output 'hello world! -> wniir praik!'

def affine_decrypt(ciphertext, a, b):
    ''' Decrypt `ciphertext` (str) as an affine cipher with given `a` and `b` 
    '''
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            char = chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
        plaintext.append(char)
    plaintext = ''.join(plaintext)
    return plaintext

ciphertext = 'wniir praik!'
a, b = 3, 1

plaintext = affine_decrypt(ciphertext, a, b)
print(ciphertext, '->', plaintext) # expected output 'wniir praik! -> hello world!'

# Load ciphertext
file_path = DATA_DIR / 'ciphertext_affine.txt'
with open(file_path, 'r') as file:
    ciphertext = file.read()

freq = letter_distribution(ciphertext)
freq = {k: v for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)}
mapping = {k: v for k, v in zip( txt_distribituin.keys(), freq.keys())}
print(mapping)

keys = list(mapping.keys())
x_1 , x_2 = (ord(keys[0]) - ord('a')) % 26 , (ord(keys[1]) - ord('a')) % 26
y_1 , y_2 = (ord(mapping[keys[0]]) - ord('a')) % 26, (ord(mapping[keys[1]]) - ord('a')) % 26

a = ((y_2 - y_1) * pow((x_2 - x_1), -1, 26)) % 26
b = (y_1 - a * x_1) % 26

if gcd(a, 26) == 1:
    decrypted = affine_decrypt(ciphertext, a, b)
    print(decrypted)
else:
    print('a is not invertible')
