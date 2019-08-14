import statistics
num=int(input())
arr=[]
for i in range(num):
	x=int(input())
	arr.append(x)
w=arr.sort()
median=statistics.median(arr)
print(median)
