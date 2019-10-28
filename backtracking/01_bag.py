# -*- coding:utf-8 -*-
# 01背包:一个背包总的承载重量是Wkg, 把重量不等的n个物品装进背包中。
#  在不超过总承载重量的前提下，让背包中物品的总重量最大
# 贪心算法中物品是可以分割的，但此问题中对每个物品来说只有两个选择,装还是不装,所以叫0-1背包问题
tmp_weight = 0  # 全局变量，用来存储bag实际存储的最大重量



def bag(i, cw, n_weight, bag_max_weight):
    if cw == bag_max_weight or i == len(n_weight):  # 递归终止条件
        global tmp_weight
        if cw > tmp_weight:
            tmp_weight = cw
        return
    
    bag(i+1, cw, n_weight, bag_max_weight)  # 递推公式:从第一个物品开始，选择不装入背包，依次递归
                                            # 一直到最后一个物品，触发递归终止条件，然后返回，就可以执行此行之后的函数了

    if cw+n_weight[i] <= bag_max_weight:
        bag(i+1, cw+n_weight[i], n_weight, bag_max_weight)


if __name__ == '__main__':
    n_weight = [2, 1, 4, 8, 3]
    max_weight = 19
    bag(0, 0, n_weight, max_weight)
    print(tmp_weight)