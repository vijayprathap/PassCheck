import re
import random

num_check = re.compile(r"[0-9]")
upp_case = re.compile(r"[A-Z]")
spl_char = set('`~!@#$%^&*()-_=+{[}]|\;:"\'<,>.?/')
password = raw_input("Enter your password: ")
print password


def sixLetter(password):
	if len(password) >= 6:
		return True
	else:
		return False
		
def hasNumber(password):
	val = num_check.search(password)
	return bool(val)

def hasUpper(password):
	val = upp_case.search(password)
	return bool(val)
	
def hasSplChar(password):
	if any((c in spl_char) for c in password):
		return True
	else:
		return False
		
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
		
def isWeakPassword(password):
	if not sixLetter(password) or not hasNumber(password) or not hasUpper(password) or not hasSplChar(password) or not notSameChar(password):
		print "The given password is not good enough"
		return True
	else:
		print "The given password is strong enough"
		return False
		
def putNumber(password):
	randindex = random.randint(0,len(password)-1)
	randnum = random.randint(0,9)
	newpass = password[:randindex] + str(randnum) + password[randindex:]
	return newpass
	
def makeCaps(password):
	randindex = random.randint(0,len(password)-1)
	c=password[randindex]
	while c.isdigit() or c in spl_char:
		print 'test'
		c=password[randindex]
		print c
		randindex = random.randint(0,len(password)-1)
		#print randindex
	print randindex
	newpass = password[:randindex]+password[randindex].upper()+password[randindex+1:]
	return newpass
	
def putSymbol(password):
	randindex = random.randint(0,len(password)-1)
	symbol=''.join(random.sample(spl_char,1))
	newpass = password[:randindex] + symbol + password[randindex:]
	return newpass
	
print makeCaps(password)
#def putCharacter(password):
	
#print hasNumber(password)
#print sixLetter(password)
#print hasUpper(password)
#print hasSplChar(password)
#print notSameChar(password) 

#isWeakPassword(password)

#print putNumber(password)

#print putSymbol(password)
"""test = "my5space"
print int(test[5])"""
