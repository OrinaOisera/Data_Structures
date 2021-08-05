def findPair(A,sum):
    x = 1
    for i in range(len(A)- 1):

        for j in range(i+1, len(A)):
            if A[i] + A[j] == sum:
                print(A[i], "&", A[j])
                # print("Pair found is at index", i, "and", j)
                print([i,j])

        # print("Pair found", x)
        # x += 1


 manumber = [2,7,11,15]
lengo = 9

findPair(A, sum)
