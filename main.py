def two_sum (arr,sum):
    x = []
    # y = []
    # y = arr[0:]
    x = arr[0:]
    arr.sort()
    left = 0
    right = len(arr) - 1

    while arr[right] > arr[left]:
        if arr[right] +arr[left] > sum:
            right = right - 1
        elif arr[right] +arr[left] < sum:
             left = left + 1
        elif arr[right] +arr[left] == sum:
            print("The values are ", arr[left] , "&", arr[right])
            left = left + 1
            right = right - 1
            print(x)
            # print(arr)
            if arr[right] in x:
                print("yes")
                n = len(x)
                i = 0
                for arr[right] in range(n):
                    if arr[right] != x[i]:
                          i = i  + 1
                    elif arr[right] == x[i]:
                        print(i)
                # for arr[right] in range(n):
                #     if arr[right] != x[i]:
                #           i = i + 1
                #     elif arr[right] == x[i]:
                #         print(i)



                    # if arr[left] != x[i]:
                    #       i = i + 1
                    # elif arr[left] == x[i]:
                    #     print(i)






                # while arr[right] in x:
                #     r = 0
                #     if arr[right] > x[r]:
                #         r = r + 1
                #     elif arr[right] == x[r]:
                #         print(x[r])









arr = [5, 7, 4, 3, 9, 8, 19, 2]
sum = 12
two_sum(arr, sum)
