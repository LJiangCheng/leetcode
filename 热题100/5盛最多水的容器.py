"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""


class Solution:
    def maxArea(self, h: list[int]) -> int:
        maxRet = 0
        # 遍历所有可能性
        for i, n in enumerate(h):
            j = i + 1
            while j < len(h):
                area = min(h[i], h[j]) * (j - i)
                maxRet = max(maxRet, area)
                j += 1
        return maxRet

    # 双指针解法
    # 说明：
    # 为什么双指针解法是对的，最关键的问题是为什么可以舍弃当前较小的边界值？
    # 核心是：最初左右指针就是在"起点"和"终点"
    # 此时较小的值即是容器在高度上的"短板"，无论另一个指针如何移动，新容器都不可能比当前容量更大
    # 因此，舍弃较小值总是正确的
    def maxArea2(self, h: list[int]) -> int:
        start = 0
        end = len(h) - 1
        maxArea = 0
        while end > start:
            maxArea = max(maxArea, min(h[start], h[end]) * (end - start))
            if h[start] > h[end]:
                end -= 1
            else:
                start += 1
        return maxArea


print(Solution().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
