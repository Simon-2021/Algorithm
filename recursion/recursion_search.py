# 输入：一个数组
# 输出：第二大的元素
# 要求：采用递归算法

# def sum(arr):
#     value = arr.pop(0)
#     print(value)
#     if not len(arr):
#         return value
#     else:
#         return value + sum(arr)

def find(arr):
    if len(arr) < 2:
        return None
    if len(arr) == 2:
    return


num_list = [1,3,5,7,9]
print(find(num_list))