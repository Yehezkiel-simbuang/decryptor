def dec(message, key) :
	if len(key) < len(message) :
		key_len = int(len(message)/len(key))
		key_len_mod = len(message)%(len(key)*key_len)
		key = (key*key_len)+key[:key_len_mod]

	if len(key) == len(message) :
		decrypted = ""
		symbol_counter = 0
		for i in range(len(message)):
			if (message[i] >= chr(65) and message[i] <= chr(90) or 
				message[i] >= chr(97) and message[i] <= chr(122)):
				
				if message[i].islower() :
					decrypted += chr((((ord(message[i])-97) - (ord(key[i-symbol_counter])-65))%26) + 97)
				
				elif(message[i].isupper()) :
					decrypted += chr((((ord(message[i])-65) - (ord(key[i-symbol_counter])-65))%26) + 65)
			
			else :
				decrypted += message[i]
				symbol_counter += 1

		print(decrypted)

msg = input("Input your encrypted message :")
key = input("Input your key :")
print("\nYour decrypted message")
dec(msg,key)