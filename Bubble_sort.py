def findPair(A,sum):
     for i in range(len(A)- 1):

        for j in range(i+1, len(A)):
             if A[i] + A[j] == sum:
                 print("Pair forund is at index", i , "and", j)

     print("Pair found")



A = [5, 7, 4, 3, 9, 8, 19, 2]
sum =12

findPair(A,sum)
