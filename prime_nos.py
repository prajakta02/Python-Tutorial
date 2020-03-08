for a in range(2,100):	#1 is nor prime not composite
	n=0
	for i in range(2,a):
		if(a%i==0):
			n=n+1
	if(n==0):
		print(a)
		

		