"""
The Vigenere cipher is a modified caesar-shift cipher wherein the key
is not a number, but an n-letter string. Each letter in the key string
specifies the cipher that shall be used to encode/decode the message.
The "x-cipher", where x is a letter, is that caesar cipher which causes
the letter 'a' to be encoded as 'x'.

Example:
plaintext -> "PLAINTEXT",
key -> "KEY",
ciphertext -> "zpysrrobr".
"""

alphabets = "abcdefghijklmnopqrstuvwxyz"

def encode(plaintext, key):
	"""
	Encodes the plaintext using the key provided and 
	returns the ciphertext.
	"""
	
	plaintext = plaintext.lower()
	key = key.lower()
	
	for i in key:
		if (ord(i)<97 or ord(i)>122) :
			return "Invalid Key: Key can only have alphabets i.e. no special characters or spaces."
	
	ciphertext = ""
	length = len(key)
	x=0
	
	for i in plaintext:
		if (alphabets.find(i) != -1):
			finalIndex = (alphabets.find(i) + ord(key[x]) - 97) % 26
			ciphertext += alphabets[finalIndex]
			if x == length - 1 :
				x = 0
			else:
				x = x + 1
		else:
			ciphertext += i
	
	return ciphertext



def decode(ciphertext, key):
	"""
	Decodes the ciphertext using the key provided and
	returns the plaintext.
	"""
	
	ciphertext = ciphertext.lower()
	key = key.lower()
	
	for i in key:
		if (ord(i)<97 or ord(i)>122) :
			return "Invalid Key: Key can only have alphabets i.e. no special characters or spaces."			
	
	plaintext = ""
	length = len(key)
	x=0
	
	for i in ciphertext:
		if (alphabets.find(i) != -1):
			if ((alphabets.find(i) - ord(key[x]) + 97) > 0):
				finalIndex = (alphabets.find(i) - ord(key[x]) + 97)
			else:
				finalIndex = (alphabets.find(i) - ord(key[x]) + 97 + 26) % 26
			plaintext += alphabets[finalIndex]
			if x == length - 1 :
				x = 0
			else : 
				x = x + 1 
		else:
			plaintext += i
	
	return plaintext

