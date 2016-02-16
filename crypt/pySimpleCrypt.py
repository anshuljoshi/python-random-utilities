#!/usr/bin/env python

# The MIT License (MIT)
#
# Copyright (c) 2016 Anshul Joshi anshuljoshi.cse@gmail.com
# license: GNU GENERAL PUBLIC LICENSE <http://www.gnu.org/licenses/gpl-3.0.html>
#
# Anshul Joshi anshuljoshi.github.io
#
# Usage: python pySimpleCrypt.py filename key flag(1->encrypt, 2->decrypt)
# or python pySimpleCrypt.py
# and provide input interactively

from Crypto.Cipher import XOR
import base64
import sys

def simpleEncrypt(key, plaintext):
	cipher = XOR.new(key)
	return base64.b64encode(cipher.encrypt(plaintext))

def simpleDecrypt(key, ciphertext):
	cipher = XOR.new(key)
	return cipher.decrypt(base64.b64decode(ciphertext))

def readf(fname):
	try:
		filestring = open(fname,"r").read()
		return filestring
	except:
		print "Unable to read file."
		exit()

def textEncrypt(text):
	try:
		key = raw_input('Enter key:  ')
		encryptedText = simpleEncrypt(key, text).decode('utf-8')
		return encryptedText
	except:
		print "Cannot encrypt."
		exit()

def textDecrypt(text):
	try:
		key = raw_input('Enter key:  ')
		decryptedText = simpleDecrypt(key, text).decode('utf-8')
		return decryptedText
	except:
		print "Cannot decrypt. Check key!"
		exit()

def fprocess(fname, key, flag):
	fileStr = open(fname,"r").read()
	outputFname = fname + "_out"
	outfname = open(outputFname,"wr+")
	if flag=='1':
		encryptedText = simpleEncrypt(key, fileStr)
		outfname.write(encryptedText)
		outfname.close()
	elif flag=='2':
		decryptedText = simpleDecrypt(key, fileStr)
		outfname.write(decryptedText)
		outfname.close()
	else:
		print "Bad Flag"
		exit()

def commandInputs():
	try:
		fname = sys.argv[1]
		key = sys.argv[2]
		flag = sys.argv[3]
		fprocess(fname, key, flag)
		print "Done!"
	except:
		print "Usage: python pySimpleCrypt.py filename key flag(1->encrypt, 2->decrypt)"
		exit()

def interactiveInputs():
	choice = raw_input('1->Encrypt or 2->Decrypt ... ?  ')
	text = raw_input("Enter text: ")
	if choice == '1':
		try:
			encryptedText = textEncrypt(text)
			print "Encrypted text: " + encryptedText
		except:
			print ('Something unexpected happened. This code is not mature.')
			exit()
	elif choice == '2':
		try:
			decryptedText = textDecrypt(text)
			print "Decrypted text: " + decryptedText
		except:
			print ('Something unexpected happened. This code is not mature.')
			exit()
	else:
		print ('Wrong choice! Booooo... Exiting.')


def main():
	if len(sys.argv)>1:
		commandInputs()
	else:
		interactiveInputs()

if __name__ == '__main__':
	main()
