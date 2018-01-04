#!/usr/bin/env python

def getMode():
    """
	Collecting mode of use: (case insensitive)
		Encrypt:
		  You can input encrypt or e
		Descrypt:
		  You can input decrypt or d
	This function requires no arguments and returns the mode in type string.
    """
    while True:
        print('Decrypt/Encrypt/quit?')
        mode = input().lower()
        if 'q' in mode:
            quit()
        elif mode in 'encrypt decrypt e d'.split():
            return mode
        else:
            print('An error occured while handling your request: %s\n Enter encrypt / decrypt' % mode)

def getMessage():
    """
	A function which requires no arguments.
	It returns the message the user types.
    """
    return input('Enter your message:\n')

def caesar(plainText, shift):
    """
	A function which takes plaintext and shift key as arguments.
	Implementation of the Ceasar shift cipher.
	It returns ciphertext string.
	It can be used in the purpose of encryption.
    """
    cipherText = ""
    for ch in plainText:
      if ch.isalpha():
        stayInAlphabet = ord(ch) + shift
        if stayInAlphabet > ord('z'):
          stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    return cipherText
def caesarDec(plainText, shift):
  """
  	A function which takes a plaintext and shift key as arguments.
	Implementation of the Caesar shift cipher.
	It returns ciphertext string.
	It can be used in the purpose of decryption.
  """
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) - shift
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  return cipherText
if __name__ == '__main__':
    print('[-] Welcome to Caesar tool for CTF use')
    print('[+] You can import this as a module and use help() for addictional data')
    mode = getMode()
    message = getMessage()
    if mode[0] == 'd':
        key = input('Please put key if you have it:')
        if key != '':
            print(caesarDec(message, int(key)))
        else:
            counter = 26
            for _ in range(0,26+1):
                print("For key %d text is %s" % (counter, caesar(message, _)))
                counter = counter - 1
    else:
        while True:
            key = input('Please put key if you have it:')
            if key == 'quit':
                quit()
            elif key != '' and int(key) in range (1,27):
                print(caesar(message, int(key)))
            else:
                print('Oops! something went wrong.')
