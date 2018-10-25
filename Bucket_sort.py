test1 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
test2 = [['Abby', 58], ['Julia', 44], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], ['Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]
test3 = {'julia': 58, 'abby': 44, 'jane': 31, 'stephen': 76}

# Basic
def bucketsort1(data):
    max_score = 100
    bucket = []
    # tmp = []
    for i in range(max_score+1):
        bucket.append(0)
        
    for score in data:
        bucket[score] = bucket[score] + 1

    index = 0
    for i in range(len(bucket)):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                data[index] = i
                index += 1
    # for i, flag in enumerate(bucket):
    #     if flag != 0 :
    #         while flag >0:
    #             tmp.append(i)
    #             flag -= 1
    # for index, score in enumerate(tmp):
    #     data[index] = score

bucketsort1(test1)
print(test1)


#---------------------------------------------------------

# Hash
def bucketsort_hash(data):
    max_score = 100
    bucket = []
    bucket_num = lambda x: int(x/33)
    
    for i in range(bucket_num(max_score)+1):
        bucket.append([])

    for x in data:
        index = bucket_num(x[1])
        bucket[index].append(x)

    for i, flag in enumerate(bucket):
        if flag != [] :
            bucket[i] = sorted(bucket[i], key=lambda x: x[1])

    index = 0
    for i in bucket:
        if i != []:
            for j in i:
                data[index] = j
                index += 1
                # print(j)
bucketsort_hash(test2)
print(test2)
#---------------------------------------------------------

# Radix sort
def radixsort(data):
    length = len(data)
    count = max(data)

    digit = 1
    while count > 9:
        count /= 10
        digit += 1

    tmp = []
    cur = 0
    for i in range(length):
        tmp.append([0] * length)
    order = [0] * length
    
    if digit <= 9: 
        '''use LSD(Least significant digit) method '''
        n = 1
        while n <= max(data):
            for i in range(length):
                lsd = int(data[i]/n) % 10
                tmp[lsd][order[lsd]] = data[i]
                order[lsd] += 1
            for i in range(length):
                if order[i] != 0 :
                    for j in range(order[i]):
                        data[cur] = tmp[i][j]
                        cur += 1
                order[i] = 0
            n *= 10
            cur = 0        
        print(data)
    
    # else:
    #     '''use MSD(Most significant digit) method '''
    #     n = pow(10, digit-1)
    #     while n >= min(data):
    #         for i in range(length):
    #             if data[i] < n:
    #                 continue
    #             else:
    #                 msd = int(data[i]/n) % 10   ##unsovled:the passed magnitude won't be recored and resorted, so the max magnitude will be repeated several times.
    #                 tmp[msd][order[msd]] = data[i]
    #                 order[msd] += 1
    #         for i in range(length):
    #             if order[i] != 0:
    #                 for j in range(order[i]):
    #                     data[cur] = tmp[i][j]
    #                     cur += 1
    #             order[i] = 0
    #         n /= 10
    #         cur = 0
    #     print(data)

radixsort(test1)
