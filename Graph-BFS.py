import numpy as np

class note:
	def __init__(self):
		self.x = np.zeros(2501, dtype=np.int)
		self.s = np.zeros(2501, dtype=np.int)

que = note()
book = np.zeros(51, dtype=np.int)
e = np.zeros((51,51), dtype=np.int)

flag = 0

n, m, start, end = map(int, input().split(' '))

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

head = 1
tail = 1

que.x[tail] = start
que.s[tail] = 0
tail += 1
book[1] = start

while head<tail :
	cur = que.x[head]
	for j in range(1, n+1):
		if e[cur][j] != 99999999 and book[j]==0 :
			que.x[tail] = j
			que.s[tail] = que.s[head] +1
			tail +=1
			book[j]=1

		if que.x[tail] == end:
			flag = 1
			break
	if flag ==1:
		break
	head += 1

print (que.s[tail-1])




