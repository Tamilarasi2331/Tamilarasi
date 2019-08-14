k1=int(input())
k2=int(input())
for i in range(k1+1,k2):
	order=len(str(i))
	sum=0
	temp=i
	while temp>0:
		dig=temp%10
		sum+=dig**order
		temp//=10
	if i==sum:
		print(i)
