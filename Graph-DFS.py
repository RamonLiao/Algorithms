import numpy as np

min1=99999999
book = np.zeros(101, dtype=np.int)
e = np.zeros((101,101), dtype=np.int)

def dfs (cur, dis):
	global min1
	if dis > min1: return
	if cur == n:
		if dis < min1: 
			min1 = dis
			return
	for j in range(1, n+1):
		if e[cur][j] != 99999999 and book[j]==0 :
			book[j]=1
			dfs(j, dis+e[cur][j])
			book[j]=0
	return

n, m = map(int, input().split(' '))
for i in range(1, n+1):
	for j in range(1, n+1):
		if i==j: 
			e[i][j]=0
		else: 
			e[i][j]=99999999

for i in range(1, m+1):
	a, b, c = map(int, input().split(' '))
	e[a][b] = c #unidirectional
	e[b][a] = c #bidirectional

book[1]=1
dfs(1, 0)
print(min1)
