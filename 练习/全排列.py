class Solution:
    def __init__(self):
        self.res = []

    # 主函数 输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: list[int]) -> list[list[int]]:
        track = []
        used = [False for _ in range(len(nums))]
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            # 一条路径遍历完毕，从栈顶向下，沿调用链返回
            self.res.append(track.copy())
            return

        for i in range(len(nums)):
            if not used[i]:
                # 选择路径
                track.append(nums[i])
                used[i] = True
                # 进入下一层决策树
                self.backtrack(nums, track, used)
                # 调用链返回的过程中，沿途撤销选择
                track.pop()
                used[i] = False


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
