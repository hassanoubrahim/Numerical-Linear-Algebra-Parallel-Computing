#matrix multupliaction


def mat_multi(a, b):
    c =  [[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k]*b[k][j]
    return c
    
a = [[1, 3], [4, 4]]
b = [[3, 4], [2, 5]]
print(mat_multi(a, b))


#output : [[9, 19], [20, 36]]


