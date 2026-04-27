"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        i = j = 0
        # 右指针往后走，遇到非0则和做指针交换值
        # 左指针交换值后往后走
        # 策略：左指针前都是非0值，左右指针之间都是0，直到右指针遍历到数组末尾
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1


nums = [0, 1, 0, 3, 0, 12]
Solution().moveZeroes(nums)
print(nums)
