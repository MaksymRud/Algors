


def Merge_CountSplit(B, C):
    i = 0
    j = 0
    count = 0
    D = []
    while i < len(B) and j < len(C):
            if B[i] > 2*B[j]:
                D.append(C[j])
                j += 1
                count += len(B[i:])
            else:
                D.append(B[i])
                i += 1
            

    while i < len(B):
        D.append(B[i])
        i += 1

    while j < len(C):
        D.append(C[j])
        j += 1

    Z = count

    return D, Z
    

def Sort_Count(A):
    length = len(A)
    if length == 1:
        return A,0
    else:
        middle = length // 2
        B,X = Sort_Count(A[:middle])
        C,Y = Sort_Count(A[middle:])
        D,Z = Merge_CountSplit(B, C)
        return D, X + Y + Z

def alg(path):
    f = open(path, "r")
    f1 = f.readlines()
    a = [int(x) for x in f1]
    
    return Sort_Count(a)[1]

print(alg("IntegerArray.txt"))