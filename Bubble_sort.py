data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
data2 = [['Abby', 58], ['Julia', 44], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], [
    'Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]

def bubblesort(data):
    # 定義資料長度
    n = len(data)
    for i in range(n-2):                               # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):                         # 從第1個開始比較直到最後一個還沒到最終位置的數字 
            if data[j] > data[j+1]:                    # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]

bubblesort(data)
print(data)

def bubblesort2(data):
    n = len(data)
    for i in range(n-2):
        for j in range(n-i-1):
            if data[j][1] > data[j+1][1]:
                data[j], data[j+1] = data[j+1], data[j]


bubblesort2(data2)
print(data2)
