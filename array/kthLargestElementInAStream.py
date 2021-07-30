from typing import List


class KthLargest:

    nums = []
    k = 1

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        if self.k >= len(self.nums):
            return self.nums[0]
        else:
            return self.nums[len(self.nums) - self.k]

# 问题 获取流中第k大的值
# 边界 k 超过 流的长度会怎么样，返回最小的即可
# 边界 流为空会怎么样 k必须为1,不然就报错

# 解决方案，每加入一个 值 之后就排序，从后往前取出 需要的值

# 实施 没想到其他方案，按上述方案实现即可

# 反馈
if __name__ == "__main__":
    # ["KthLargest", "add", "add", "add", "add", "add"]
    # [[1, []], [3], [5], [10], [9], [4]]

    # print("HelloWorld")
    # [null, 3, 5, 10, 10, 10]



    # kthlargest = KthLargest(1,[])
    # for i in [3,5,10,9,4]:
    #     print(kthlargest.add(i))


    kthlargest = KthLargest(3, [4, 5, 8, 2])
    # 预期
    # [null,4,5,5,8,8]
    for i in [3,5,10,9,4]:
        print(kthlargest.add(i))