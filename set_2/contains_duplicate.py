class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       # O(n^2)

        # duplicate = nums
        # cotains_duplicate=False
        # length = len(nums)
        # for i in range(length):
        #     temp = duplicate[i]
        #     duplicate[i]= None
        #     if (temp in duplicate) :
        #         cotains_duplicate=True
        #         break
        # return cotains_duplicate

        # O(n)

        # set_of_integers=set ()
        # for i in nums:
        #     if i not in set_of_integers :
        #         set_of_integers.add(i)
        #     else :
        #         return True
        # return False

        # faster approach
        return len(nums) != len(set(nums))
