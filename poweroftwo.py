def checkIfPowerOf2(n):
	if(n==1):
		print "true"
	n%2==0 and checkIfPowerOf2(n/2)


n = int(input("Enter a number: "))
checkIfPowerOf2(n)	


