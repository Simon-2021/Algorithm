# 输入：一个无序数组
# 输出：一个从小到大的有序数组

# 快速排序，递归地将数组分配到不同侧


def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    else:
        arr_low = []
        arr_high = []
        for i in range(len(arr)):
            if arr[i] < arr[0]:
                arr_low.append(arr[i])
            if arr[i] > arr[0]:
                arr_high.append(arr[i])
        return quick_sort(arr_low) + [arr[0]] + quick_sort(arr_high)


num_list = [51, 30, 23, 1, 3, 14, 5, 7, 9]
print(quick_sort(num_list))