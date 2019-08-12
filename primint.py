n1=int(input())
k=int(input())
for num in range(n1+1,k):
	if num>1:
		for n in range(2,num):
			if(num%n)==0:
				break
		else:
			print(num)
