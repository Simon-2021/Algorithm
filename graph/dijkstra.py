# 狄克斯特拉算法寻找最优路径

import sys

# 简历各散列表
# 图关系表
graph = {}
graph['start'] = {'a': 6, 'b': 2}
graph['a'] = {'end': 1}
graph['b'] = {'a': 3, 'end': 5}
graph['end'] = {}

# 开销表
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# 父节点表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# 已处理列表
processed = []

# 计算当前开销最低且未被处理过的节点
def find_lowcost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_node = None
    # 遍历开销表
    for node in costs:
        cost = costs[node]
        # 当节点开销小于当前最小开销，且未被处理
        if cost < lowest_cost and node not in processed:
            # 更新最小开销和节点
            lowest_cost = cost
            lowest_node = node
    return lowest_node

# 计算最小开销节点
node = find_lowcost_node(costs, processed)
while node is not None:
    # 计算当前节点的邻居
    neighbor = graph[node]
    # 遍历当前节点的邻居
    for n in neighbor.keys():
        # 计算当前邻居的开销
        new_cost = costs[node] + neighbor[n]
        # 当新开销小于旧开销时
        if new_cost < costs[n]:
            # 更新该邻居的开销
            costs[n] = new_cost
            # 更新该邻居的最优父节点
            parents[n] = node
    # 将当前节点加入已处理列表
    processed.append(node)
    # 计算下一个节点
    node = find_lowcost_node(costs, processed)


print(costs['end'])


