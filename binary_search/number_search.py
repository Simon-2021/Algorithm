# 输入：一个正向有序数字列表，一个数字
# 输出：该数字在列表中的下标，或NULL（当列表中不存在该数字时）

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low + high)/2)
        if list[mid] > item:
            high = mid - 1
        elif list[mid] < item:
            low = mid + 1
        else:
            return mid
    return None

mylist = [1,3,5,7,9]
print(binary_search(mylist,9))