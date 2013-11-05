import re

num_check = re.compile(r"[0-9]")
upp_case = re.compile(r"[A-Z]")
spl_char = set('`~!@#$%^&*()-_=+{[}]|\;:"<,>.?/')
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
	count = 0
	for i in password:
		for j in range(password.index(i)+1,len(password)):
			if i is password[j]:
				count+=1
				c=password[j]
	print count
	if count>1:
		print 'character %s is repeated twice' % c
		return False
	else:
		return True
		
def checkPassword(password):
	if not sixLetter(password) or not hasNumber(password) or not hasUpper(password) or not hasSplChar(password) or not notSameChar(password):
		print "The given password is not good enough"
		return True
	else:
		print "The given password is strong enough"
		return False
		
print hasNumber(password)
print sixLetter(password)
print hasUpper(password)
print hasSplChar(password)
print notSameChar(password) 

checkPassword(password)
