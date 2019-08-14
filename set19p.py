def findSum(N, K):
	ans=0;
	for i in range(1,N+1):
		ans+=(i%K)
	return ans;
N=int(input())
k=int(input())
print(findSum(N,k));
