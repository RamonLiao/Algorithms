import numpy as np
e = np.zeros((101,101), dtype=np.int)
book = np.zeros((101), dtype=np.int)
sum1 =0

def dfs (cur):
	print(cur)
	global sum1
	sum1 += 1 
	if sum1==n:
		return
	for i in range(1, n+1):
		if e[cur][i]==1 and book[i]==0 :
			book[i]=1
			dfs(i)		
	return


n, m = map(int, input().split(' '))
for i in range(1, n+1):
	for j in range(1, n+1):
		if i==j : 
			e[i][j]=0
		else: 
			e[i][j]=99999999
for i in range(1, m+1):
	a, b = map(int, input().split(' '))
	e[a][b]=1
	e[b][a]=1

book[1]=1
dfs(1)




