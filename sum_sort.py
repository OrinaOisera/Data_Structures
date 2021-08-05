
def two_sum(arr, sum):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while arr[left] < arr[right] :
        if arr[left] + arr[right] < sum:
            left = left + 1
        elif arr[left] + arr[right] > sum:
            right = right - 1
        elif arr[left] + arr[right] == sum:
            print("The values are ", arr[right] , "&" , arr[left])
            right = right - 1
            left = left + 1



arr = [5, 7, 4, 3, 9, 8, 19, 21]
sum = 17
two_sum(arr, sum)

