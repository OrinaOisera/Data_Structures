def findPair(A,sum):
    x = 1
    for i in range(len(A)- 1):

        for j in range(i+1, len(A)):
            if A[i] + A[j] == sum:
                print(A[i], "&", A[j])
                print("Pair found is at index", i, "and", j)

        print("Pair found", x)
        x += 1


A = [5, 7, 4, 3, 9, 8, 19, 2]
sum =12

findPair(A, sum)
