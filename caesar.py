#!/usr/bin/env python

def getMode():
    while True:
        print('Decrypt/Encrypt?')
        mode = input().lower()
        if mode in 'encrypt decrypt e d'.split():
            return mode
        else:
            print('An error occured while handling your request: %s\n Enter encrypt / decrypt' % mode)

def getMessage():
    return input('Enter your message:\n')

def caesar(plainText, shift):
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  return cipherText

mode = getMode()
message = getMessage()
if mode[0] == 'd':
    key = input('Please put key if you have it:')
    if key != '':
        print(caesar(message, int(key)))
    else:
        for _ in range(0,26+1):
            print("For key %d text is %s" % (_, caesar(message, _)))
else:
    while True:
        key = input('Please put key if you have it:')
        if key == 'quit':
            quit()
        elif key != '' and int(key) in range (1,27):
            print(caesar(message, int(key)))
        else:
            print('Oops! something went wrong.')
