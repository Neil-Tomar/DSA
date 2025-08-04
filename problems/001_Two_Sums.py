def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen={}
        for index ,value in enumerate(nums):
            if target - value in seen:
                  return [seen[target-value],index]
            seen[value]=index


print(twoSum([2,7,11,15],9))