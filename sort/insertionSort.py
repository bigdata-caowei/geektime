#   基于Python实现插入排序
#   Author: AllenGFLiu
#   插入排序实现原理：
#   把原始list当成两部分看待：已排序的和未排序的
#   最开始时把原始list的第一位默认作为已排好序的唯一一个元素，取未排序的第一个元素（value)与之对比
#   如果排序元素大于未排序元素，则把该排序元素移动到未排序元素的位置
#   注意，未排序的第一个元素与前面已排好序的元素对比时，是从后往前依次对比的，因为都是已经排好序的
#   插入排序是原地原地算法，也是稳定算法
#   因为比冒泡排序有更少的赋值动作，所以插入排序比冒泡排序用的更多一点

def insertionSort(myList):
    length = len(myList)
    if length <= 1:
        return

    for i in range(length)[1:]:
        j = i - 1
        while j >= 0:
            if myList[j] > myList[j+1]:
                # 只有当后一个元素比前面的元素小时，才会产生移动
                myList[j+1], myList[j] = myList[j], myList[j+1]
            else:
                break
            j -= 1

if __name__ == "__main__":
    List = [3, 1, 2, 8, 4]
    print('排序前:')
    print(List)
    insertionSort(List)
    print('排序后:')
    print(List)   