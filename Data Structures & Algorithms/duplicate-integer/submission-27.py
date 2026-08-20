class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set_nums = set()
        # for num in nums:
        #     if num in set_nums:
        #         return True
        #     set_nums.add(num)
        # return False

        # return False if len(set(nums)) == len(nums) else True

        # sorted_num = sorted(nums)
        # for num in range(len(nums)):
        #     for num_in in range(num+1,len(nums)):
        #         if nums[num]==nums[num_in]:
        #             return True
        # return False 
        sorted_num = sorted(nums)
        for num in range(len(sorted_num)-1):
            curr = num
            nex = num+1
            if sorted_num[curr]==sorted_num[nex]:
                return True
        return False
