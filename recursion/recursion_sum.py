# 输入：一个数组
# 输出：数组的和
# 要求：采用递归算法

def sum(arr):
    value = arr.pop(0)
    print(value)
    if not len(arr):
        return value
    else:
        return value + sum(arr)

num_list = [1,3,5,7,9]
print(sum(num_list))