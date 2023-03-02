import random

# Globals
alpha = []
cipher = []
message = "HELLO THERE SPACE COMANDER"

def make_cipher():
  #initial alpha and cipher
  for i in range(26):
    alpha.append(chr(ord('A') + i))
    cipher.append('')

  #LOL THIS IS JUST SHUFFLE FOUND THAT OUT TOO LATE
  for i in range(26):
    j = random.randint(0,25)
    while True:
      if cipher[j] == '':
        break
      j = random.randint(0,25)
    cipher[j] = alpha[i]
    

def encrypt(message):
  encrypted = ""
  for letter in message:
    if letter in alpha:
      index = ord(letter) - ord('A')
      encrypted += cipher[index]
    else:
      encrypted += letter

  return encrypted


make_cipher()
# print(alpha)
# print(cipher)
print(message)
print(encrypt(message))