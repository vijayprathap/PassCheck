password = raw_input("Enter your password: ")
print password

def sixLetter(password):
	if len(password) >= 6:
		return True
	else:
		return False
		
def hasNumber(password):
	count=0
	for j in password:
		if j==str(0) or j==str(1) or j==str(2) or j==str(3) or j==str(4) or j==str(5) or j==str(6) or j==str(7) or j==str(8) or j==str(9):
			count+=1
		print count
	print count	
	if count>0:
		return True
	else:
		return False
			
print hasNumber(password)
print sixLetter(password)
