def binary(arr,lb,ub,value):
    if lb <0:
        print("Data not Found")
        return
    mid = (lb+ub)//2
    # print(mid)
    if arr[mid] == value:
        print("Data Found")
    elif value>arr[mid]:
        binary(arr,mid+1,ub,value)
        
    elif value<arr[mid]:
        binary(arr,lb,mid-1,value)
        

arr = [11, 12, 14, 19, 23, 76, 78, 91]
binary(arr,0,len(arr)-1,11)