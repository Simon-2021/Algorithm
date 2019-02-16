# 输入：一个数组
# 输出：数组的最大值
# 要求：采用递归算法

def max(arr):
    value = arr.pop(0)
    if len(arr):
        x = max(arr)
        if value < x:
            value = x
    return value

num_list = [1,14,3,26,5,7,9]
print(max(num_list))