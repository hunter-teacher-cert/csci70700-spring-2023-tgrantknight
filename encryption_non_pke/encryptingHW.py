import random

# Globals
alpha = []
cipher = []

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
    
  


make_cipher()
print(alpha)
print(cipher)