def vigenere_encrypt(msg, key):
	alphabet = [
	"A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
	"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
	"U", "V", "W", "X", "Y", "Z"
	]

	plaintext = [x for x in msg]
	cipher = [x for x in key]

	keystream = []
	count = 0
	for x in plaintext:
		if x == " ":
			keystream.append(" ")
		else:
			if len(cipher) - 1 >= count:
				keystream.append(cipher[count])
				count += 1
			else:
				count += -count
				keystream.append(cipher[count])
				count += 1

	ciphertext = []
	cnt = 0
	for x in keystream:
		if x == " ":
			ciphertext.append(" ")
			cnt += 1
		else:
			newindex = (alphabet.index(x) + alphabet.index(plaintext[cnt])) % 26
			ciphertext.append(alphabet[newindex])
			cnt += 1
			
	encryptedmsg = ""
	encryptedmsg = encryptedmsg.join(ciphertext)
			
	return encryptedmsg