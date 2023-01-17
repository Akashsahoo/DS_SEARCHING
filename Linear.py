def linear(arr,value):
    n = len(arr)
    for i in range(n):
        if arr[i] == value:
            return i
    print("Data not found")

arr = [23,12,78,11,91,81,40]
print(linear(arr,40))