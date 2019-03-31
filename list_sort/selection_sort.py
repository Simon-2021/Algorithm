# 输入：一个无序数组
# 输出：一个从小到大的有序数组

# 选择排序，不断地在数组中寻找最小值，放到排序列表中，直至数组中元素个数为0

def find_smallest(arr):
    low_index = 0
    low = arr[low_index]
    for i in range(len(arr)):
        if arr[i] < low:
            low_index = i
            low = arr[low_index]
    return low_index

def selection_sort(arr):
    new_arr = []
    while len(arr):
        low_index = find_smallest(arr)
        new_arr.append(arr.pop(low_index))
    return new_arr

num_list = [1,3,14,5,7,9]
print(selection_sort(num_list))