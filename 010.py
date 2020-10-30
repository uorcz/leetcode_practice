class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        len_nums = len(nums)
        nums.sort()
        def dfs(re,index):
            if re not in res:
                res.append(re)
            for i in range(index,len_nums):
                dfs(re+[nums[i]],i+1)
        dfs([],0)
        return res