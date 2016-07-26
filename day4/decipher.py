#declare dictionary
dictionary = []


#decrypt message with a given key
def decrypt(message, key):
	#initialize empty string
	decrypted_word = ""
	# loop through characters in message
	for i in message:
		#Decrypt individual with key
		char = ord(i)
		#Uppercase letters
		if char >= 65 and char <= 90:
			char = 65 + (char - 65 - key) % 26
			decrypted_word += chr(char)
		#Lowercase letters
		elif char >= 97 and char <= 122:
			char = 97 + (char - 97 - key) % 26
			decrypted_word += chr(char)
		#symbols are left untouched
		else:
			decrypted_word += i
	return decrypted_word

#find correct decryption key
def find_key(message):
	cur_key = 1
	key_occurences = []
	for i in range (0, 27):
		key_occurences.append(0)
	while cur_key < 27:
		decrypted_message = decrypt(message, cur_key)
		words = decrypted_message.split()
		for word in words:
			if spell_checker(word):
				key_occurences[cur_key] += 1
		cur_key += 1
	most_occurences = 0
	for i in range (1, 27):
		if key_occurences[i] > most_occurences:
			cur_key = i
			most_occurences = key_occurences[i]

	return cur_key;

#loads dictionary into a list to be search for spell checker
def load_dictionary():
	txt = open("/usr/share/dict/words")
	global dictionary
	dictionary = [line.rstrip('\n') for line in txt]

#uses global dictionary list to check if word parameter is a word.
#returns true if word is in the dictionary, else false
def spell_checker(cur_word):
	global dictionary
	word = cur_word.lower()
	#initializes empty string for normalized word
	stripped_word = ""
	#loops through each word, only adding characters
	for letter in range (0,len(word)):
		#current char
		char = ord(word[letter])
		#set previous char
		if letter > 0:
			char_prev = ord(word[letter - 1])
		else:
			char_prev = 0
		#set next char
		if letter < len(word) - 1:
			char_after = ord(word[letter+1])
		else:
			char_after = 0
		#check if current char is a letter or if it is between two letters
		if (char >= 97 and char <= 122):
			stripped_word += word[letter]
		elif ((char_prev >= 97 and char_prev <= 122) and (char_after >= 97 and char_after <= 122)):
			stripped_word += word[letter]
	#check if the normalized word is in the dictionary
	return stripped_word in dictionary


#wrapper method that combines all the components of deciphering a key
def decipher(message):
	load_dictionary()
	#find the decryption key
	correctkey = find_key(message)
	#decrypt the message with the decryption key
	return decrypt(message, correctkey)


encrypted = raw_input("Please enter an encrypted message: ")
print decipher(crypted)
