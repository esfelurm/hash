#کس مادر ادیتور
import os
import sys

os.system("pip install colored")
os.system("pip install colorama")
os.system("pip install datetime")

from colorama import Fore
import hashlib
from base64 import b64encode, b64decode
import codecs
import time
import binascii
import re
from time import sleep
from platform import python_version


Limpar = "clear"

if sys.version_info[0] < 3:
	versao = python_version()
	print("\n Amir esfelurm " %(versao))


def Apresentacao():
	os.system(Limpar)
time.sleep(1)
print (Fore.YELLOW + "")
x = """
_____ ____  _____ _____ _    _   _ ____  __  __
| ____/ ___||  ___| ____| |  | | | |  _ \|  \/  |
|  _| \___ \| |_  |  _| | |  | | | | |_) | |\/| |
| |___ ___) |  _| | |___| |__| |_| |  _ <| |  | |
|_____|____/|_|   |_____|_____\___/|_| \_\_|  |_|

       \033[1mchannel Rubika : esfelurm





"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

def Again(frase, call):
	opcao1 = input(frase)
	if opcao1 == "y":
		call()
	elif opcao1 == "n":
		Escolha()
	else:
		Again(frase,call)


def Escolha():
	Apresentacao()
	print(Fore.GREEN + """
==============================================
		
	Md5 [1]
	
	Sh1 [2]
	
	Sha224 [3]
	
	Sha256 [4]
	
	Sha385 [5]
	
	Sh512 [6]
	
	Base64 [7]
	
	Binario [8]
	
	Hexadecimal [9]
	
	CifraDeCesar [10]
	
	TextReverse [11]
	
	WordsReverse [12]
	
	Exit [0]
	
  
╦╤─ ҉ - -----💥

	
==============================================

""")
	opcao1 = input("\n number =>> : ")
	if opcao1 == "1" or opcao1 == "۱":
		Md5()
	elif opcao1 == "2" or opcao1 == "۲":
		Sha1()
	elif opcao1 == "3" or opcao1 == "۳":
		Sha224()
	elif opcao1 == "4" or opcao1 == "۴":
		Sha256()
	elif opcao1 == "5" or opcao1 == "۵":
		Sha384()
	elif opcao1 == "6" or opcao1 == "۶":
		Sha512()
	elif opcao1 == "7" or opcao1 == "۷":
		Base64()
	elif opcao1 == "8" or opcao1 == "۸":
		Binario()
	elif opcao1 == "9" or opcao1 == "۹":
		Hexadecimal()
	elif opcao1 == "10" or opcao1 == "۱۰":
		CifraDeCesar()
	elif opcao1 == "11" or opcao1 == "۱۱":
		TextReverse()
	elif opcao1 == "12" or opcao1 == "۱۲":
		WordsReverse()
	elif opcao1 == "0" or opcao1 == "۰":
		exit(1)
	else:
		Escolha()

def Md5():
	Apresentacao()
	mystring = input("\n TEXT ENCRYPT  MD5 : ")
	hash_object = hashlib.md5(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n edame midid (y/n) ?  ", Md5)

def Sha1():
	Apresentacao()
	mystring = input("\n TEXT ENCRYPT SHA1 :")
	hash_object = hashlib.sha1(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\nedame midi (y/n) ?", Sha1)

def Sha224():
	Apresentacao()
	mystring = input("\n  TEXT ENCRYPT SHA224 :")
	hash_object = hashlib.sha224(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\nedame midi (y/n) ? ", Sha224)

def Sha256():
	Apresentacao()
	mystring = input("\n TEXT ENCRYPT SHA256 :")
	hash_object = hashlib.sha256(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\nedame midi (y/n) ?", Sha256)

def Sha384():
	Apresentacao()
	mystring = input("\n TEXT ENCRYPT SHA384 : ")
	hash_object = hashlib.sha384(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\nedame midi (y/n) ?", Sha384)

def Sha512():
	Apresentacao()
	mystring = input("\n TEXT ENCRYPT SHA512 :")
	hash_object = hashlib.sha512(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\nedame midi (y/n) ?", Sha512)

def Base64Encode():
	Apresentacao()
	mystring = str(input("\n TEXT TRANSFORM BASE64 :")) 
	print("")
	encode = b64encode(mystring.encode('utf-8')) 
	decode = encode.decode('utf-8')
	print(decode)
	print("") 
	Again("\nedame midi (y/n) ? ", Base64Encode)

def Base64Decode():
	Apresentacao()
	mystring = str(input("\n TEXT UNCOVER BASE64 :")) 
	print("")
	try:
		decode = b64decode(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n INCORRECT PADDING :")
		sleep(3)
		Base64Decode() 
	Again("\nedame midi (y/n) ? , Base64Decode")

def Base64():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> : ")
	if opcao1 == "1":
		Base64Encode()
	elif opcao1 == "2":
		Base64Decode()
	else:
		Base64()


def BinarioEncode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		mystring = input("\n TEXT TRANSFORM BINARIO")
		print("")
		bits = bin(int(binascii.hexlify(mystring.encode(encoding, errors)), 16))[2:]
		print(bits.zfill(8 * ((len(bits) + 7) // 8)))
		print("")
	except:
		print("\nERROR")
		sleep(3)
		BinarioEncode()
	Again("\nedame midi (y/n) ? ", BinarioEncode)

def BinarioDecode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		binario = input("\n TEXT UNCOVER BINARY")
		binario = binario.replace(" ", "")
		n = int(binario, 2)
		print("")
		print(int2bytes(n).decode(encoding, errors))
		print("")
	except:
		print("\n ERROR")
		sleep(3)
		BinarioDecode()
	Again("\nedame midi (y/n) ? ", BinarioDecode)

def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def Binario():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] Kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> : ")
	if opcao1 == "1":
		BinarioEncode()
	elif opcao1 == "2":
		BinarioDecode()
	else:
		Binario()


def HexaEncode():
	Apresentacao()
	mystring = input("\n TEXT TRANSFORM HEXADECIMAL :")
	print("")
	encode = binascii.hexlify(bytes(mystring, "utf-8"))
	encode = str(encode).strip("b")
	encode = encode.strip("'")
	encode = re.sub(r'(..)', r'\1 ', encode).strip()
	print(encode)
	print("")
	Again("\nedame midi (y/n) ? ", HexaEncode)

def HexaDecode():
	Apresentacao()
	try:
		mystring = input("\n TEXT UNCOVER HEXADECIMAL :")
		print("")
		decode = bytes.fromhex(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n ERROR")
		sleep(3)
		HexaDecode()
	Again("\nedame midi (y/n) ? ", HexaDecode)

def Hexadecimal():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> : ")
	if opcao1 == "1":
		HexaEncode()
	elif opcao1 == "2":
		HexaDecode()
	else:
		Hexadecimal()


def TextReverseEncode():
	Apresentacao()
	mystring = input("\n TEXT REVERSE : ")
	print("")
	print(mystring[::-1])
	print("")
	Again("\nedame midi (y/n) ? ", TextReverseEncode)


def TextReverseDecode():
	Apresentacao()
	mystring = input("\n TEXT UNCOVER REVERSE :")
	print("")
	print(mystring[::-1])
	print("")
	Again("\nedame midi (y/n) ? ", TextReverseDecode)

def TextReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> :")
	if opcao1 == "1":
		TextReverseEncode()
	elif opcao1 == "2":
		TextReverseDecode()
	else:
		TextReverse()


def WordsReverseEncode():
	Apresentacao()
	mystring = input("\n TEXT REVERSE : ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\nedame midi (y/n) ? ", WordsReverseEncode)

def WordsReverseDecode():
	Apresentacao()
	mystring = input("\nTEXT UNCOVER REVERSE : ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\nedame midi (y/n) ? ", WordsReverseDecode)

def WordsReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> :")
	if opcao1 == "1":
		WordsReverseEncode()
	elif opcao1 == "2":
		WordsReverseDecode()
	else:
		WordsReverse()


def CifraDeCesar():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] kodam ?
\033[31m1\033[1;m) ENCODE 
\033[31m2\033[1;m) DECODE 
""")
	opcao1 = input("\n =>> :")
	if opcao1 == "1":
		ChamarBloco1()
	elif opcao1 == "2":
		ChamarBloco2()
	else:
		CifraDeCesar()


def cifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado


def decifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def ChamarBloco1():
	Apresentacao()
	try:
		c = str(input('\n TEXT CIPHER ')).lower()
		n = int(input('\nNUMERICAL KEY  '))
		print("\nRESULT", cifrar(c, n))
		print("")
	except:
		print("\n ERROR")
		sleep(3)
		ChamarBloco1()
	Again("\nedame midi (y/n) ? ", ChamarBloco1)


def ChamarBloco2():
	Apresentacao()
	try:
		cc = str(input('\nTEXT DECODE')).lower()
		cn = int(input('\nNUMERICAL KEY '))
		print("\nRESULT", decifrar(cc, cn))
		print("")
	except:
		print("\n ERROR")
		sleep(3)
		ChamarBloco2()
	Again("\nedame midi (y/n) ?", ChamarBloco2)


Escolha()
