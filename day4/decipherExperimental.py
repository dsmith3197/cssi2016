#declare dictionary
dictionary = []


#decrypt message with a given key
def decrypt(message, key):
	decrypted_word = ""
	for i in range (0, len(message)):
		#Decrypt word with key
		char = ord(message[i])
		#Uppercase letters
		if char >= 65 and char <= 90:
			char = 65 + (char - 65 - key) % 26
			decrypted_word += chr(char)
		#Lowercase letters
		elif char >= 97 and char <= 122:
			char = 97 + (char - 97 - key) % 26
			decrypted_word += chr(char)
		#symbols
		else:
			decrypted_word += message[i]
	return decrypted_word

#find correct decryption key
def findKey(message):
	cur_key = 1
	key_occurences = []
	for i in range (0, 27):
		key_occurences.append(0)
	while cur_key < 27:
		decrypted_message = decrypt(message, cur_key)
		words = decrypted_message.split()
		for word in words:
			if spellChecker(word):
				key_occurences[cur_key] += 1
		cur_key += 1
	most_occurences = 0
	for i in range (1, 27):
		if key_occurences[i] > most_occurences:
			cur_key = i
			most_occurences = key_occurences[i]

	return cur_key;

def loadDictionary():
	txt = open("/usr/share/dict/words")
	global dictionary
	dictionary = [line.rstrip('\n') for line in txt]

def spellChecker(word):
	global dictionary
	stripped_word = ""
	for letter in word:
		char = ord(letter)
		if (char >= 65 and char <= 90) or (char >= 97 and char <= 122):
			stripped_word += letter
	if stripped_word.lower() in dictionary:
		return True
	else:
		return False

def decipher(message):
	loadDictionary()
	correctkey = findKey(message)
	return decrypt(message, correctkey)


crypted = raw_input("Please enter an encrypted message: ")
print decipher(crypted)

