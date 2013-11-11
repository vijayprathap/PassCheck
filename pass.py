import re
import random

num_check = re.compile(r"[0-9]")
upp_case = re.compile(r"[A-Z]")
spl_char = set('`~!@#$%^&*()-_=+{[}]|\;:"\'<,>.?/')

#checks if the given password has atleast 6 characters
def sixLetter(password):
	if len(password) >= 6:
		return True
	else:
		return False


#checks if the given password has a number		
def hasNumber(password):
	val = num_check.search(password)
	return bool(val)


#checks if the given password has a upper case character
def hasUpper(password):
	val = upp_case.search(password)
	return bool(val)

	
#checks if the given password has a spl character
def hasSplChar(password):
	if any((c in spl_char) for c in password):
		return True
	else:
		return False


#checks if a character in password is not repeated more than twice
def notSameChar(password):
	ismore=False
	for i in password:
		count=0
		for j in range(password.index(i)+1,len(password)):
			if i is password[j]:
				count+=1
				c=password[j]
			if count>1:
				ismore=True
	if ismore:
		print 'character %s is repeated more than twice' % c
		return False
	else:
		return True
		

#checks if the given password is weak or strong
def isWeakPassword(password):
	if not sixLetters or not number or not hasUpperCase or not splChar or sameChar:
		print "\nThe given password is not good enough"
		return True
	else:
		print "\nThe given password is strong enough"
		return False
		
#inserts a random number in the password string
def putNumber(password):
	randindex = random.randint(0,len(password)-1)
	randnum = random.randint(0,9)
	newpass = password[:randindex] + str(randnum) + password[randindex:]
	return newpass
	
#changes a random character to uppercase
def makeCaps(password):
	randindex = random.randint(0,len(password)-1)
	c=password[randindex]
	while c.isdigit() or c in spl_char:
		randindex = random.randint(0,len(password)-1)
		c=password[randindex]
	newpass = password[:randindex]+password[randindex].upper()+password[randindex+1:]
	return newpass
	
#inserts a spl character randomly
def putSymbol(password):
	randindex = random.randint(0,len(password)-1)
	symbol=''.join(random.sample(spl_char,1))
	newpass = password[:randindex] + symbol + password[randindex:]
	return newpass

#gives information about your password	
def genReport(password):
	print "\nThe given password has six characters: %s" %sixLetters
	print "\nThe given password has a number: %s" %number
	print "\nThe given password has an uppercase character: %s" %hasUpperCase
	print "\nThe given password has a special character: %s" %splChar
	print "\nThe given password has a character repeated more than twice: %s" %sameChar
	
#gives you secure password
def fixPassword(password):
	if not number:
		password=putNumber(password)
	if not hasUpperCase:
		password=makeCaps(password)
	if not splChar:
		password=putSymbol(password)
	st = "\nThe suggested password is %s" %password
	return st
		
	
while True:
	print "Password should be atleast 6 characters\n"
	password = raw_input("Enter your password: ")
	if sixLetter(password) and notSameChar(password):
		break
	
sixLetters=sixLetter(password)
number = hasNumber(password)
hasUpperCase = hasUpper(password)
splChar = hasSplChar(password)
sameChar = not notSameChar(password)

genReport(password)
if isWeakPassword(password):
	print fixPassword(password)
