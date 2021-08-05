def findPair( manumber,lengo):
    x = 1
    for i in range(len(manumber)- 1):

        for j in range(i+1, len(manumber)):
            if manumber[i] + manumber[j] == lengo:
                print(manumber[i], "&", manumber[j])
                # print("Pair found is at index", i, "and", j)
                print([i,j])

                return i,j

        # print("Pair found", x)
        # x += 1


manumber = [2, 7, 11, 15]
lengo = 9

findPair(manumber,lengo )
