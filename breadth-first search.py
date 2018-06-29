import numpy as np

# import time

e = np.zeros((101,101), dtype=np.int)
book = np.zeros((101), dtype=np.int)
que = np.zeros((10001), dtype=np.int)

n, m = map(int, input().split(' '))
for i in range(1, n+1):
	for j in range(1, n+1):
		if i==j: 
			e[i][j]=0
		else:
			e[i][j]=99999999

for i in range(1, m+1):
	a, b = map(int, input().split(' '))
	e[a][b]=1
	e[b][a]=1

head=1
tail=1

que[tail]=1
tail +=1
book[1]=1

# start = time.clock()
while head<tail:
	cur = que[head]
	for i in range(1, n+1):
		if e[cur][i]==1 and book[i]==0:
			que[tail]=i
			tail +=1
			book[i]=1
		if tail > n:
			break
	if tail > n:
		break
	head += 1
	
# end = time.clock()
# print(end-start)

for i in range(1, tail):
	print(que[i])


