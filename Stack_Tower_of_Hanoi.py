#1
#https://openhome.cc/Gossip/AlgorithmGossip/HanoiTower.htm
def hanoi(n, A, B, C):
    if n == 1:
        return [(A, C)]
    else:
        return hanoi(n-1, A, C, B) + hanoi(1, A, B, C) + hanoi(n-1, B, A, C)


n = input("Please enter integer:")
for move in hanoi(int(n), 'A', 'B', 'C'):
    print("move %c to %c" % move)


#2
#http: // pythonnote.blogspot.com/2014/09/tower-of-hanoi-algorithm-analysis.html
# def hanoi(n, A="A", B="B", C="C"):
#     if n > 0:
#         hanoi(n-1, A, C, B)
#         print "Move a Disc from %s to %s" % (A, C)
#         hanoi(n-1, B, A, C)

# if __name__ == '__main__':
#     hanoi(input('How many disks you wanna play? '))



#3
#https://itw01.com/GCSTE6A.html
# def hanoi(n, A, B, C): 
#     if n == 1: 
#         print(A+'->'+C) 
#     else: 
#         hanoi(n-1, A, C, B) 
#         print(A+'->'+C) 
#         hanoi(n-1, B, A, C) 

# hanoi(3, 'A', 'B', 'C')



#4
#http://kailotus.blogspot.com/2018/05/python22hanoi.html
# def hanoi(n, A, B, C):
#     if n == 1:
#         print(str(n) + "號圈：" + A + "→" + C)
#     else:
#         hanoi(n-1, A, C, B)
#         print(str(n) + "號圈：" + A + "→" + C)
#         hanoi(n-1, B, A, C)


# ringNum = int(input("請輸入圈圈數："))
# hanoi(ringNum, "A", "B", "C")

## 執行結果：
## 請輸入圈圈數：3
## 1號圈：A→C
## 2號圈：A→B
## 1號圈：C→B
## 3號圈：A→C
## 1號圈：B→A
## 2號圈：B→C
## 1號圈：A→C
