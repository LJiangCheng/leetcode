"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]：
满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为0
"""


class Solution:
    """
    暴力循环：三重循环嵌套 时间复杂度n^3
    优化思路：
    先将数组排序才能进行后续处理。
    由于数组已排序，当j递增的时候，当前k下标右侧的值不可能再达成i+j+k=0的效果，因为k当前位置就是j递增前i+j+k对应的最小值
    可以将第三重循环和第二重循环并列执行，第三重循环从后往前，找到即截止
    像这种随着第一个元素的递增，第二个元素是递减的，就可以用双指针的方法。
    时间复杂度：第一重循环n * 第二+第三重n = n^2    排序的nlogn不影响复杂度量级
    """

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        # 先将数组排序
        nums.sort()
        ret = list()
        for i in range(n):
            first = nums[i]
            # 为去除重复值，跳过相同的数
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # 第三重循环的指针定义在这里
            k = n - 1
            for j in range(i + 1, n):
                second = nums[j]
                # 跳过相同的数
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                # 第三重循环，从最后往前，即从大往小遍历
                while k > j and first + second + nums[k] > 0:
                    k -= 1
                # 第三重循环结束，判断本轮i、j条件下的结果
                if k == j:
                    # 如果j、k重合，说明后续随着j的增加也不可能有k满足条件，可直接结束二轮循环
                    break
                if first + second + nums[k] == 0:
                    ret.append([first, second, nums[k]])
        return ret


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
