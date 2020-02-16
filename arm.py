def armstrong_fun(a):
	b = [int(x) for x in str(a)] 

	sum=0

	for k in b:

		sum=sum+k*k*k

	if(sum==a):
		return 1
	else:
		return 0		

print("Enter number you want to find armstrong number for: ")
a=int(input())
#print(" Your number is: ")
result=armstrong_fun(a)
if(result==1):
	print("Armstrong number")
else:
	print("Not an armstrong number")
	
