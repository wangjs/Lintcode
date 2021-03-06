'''
给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。

思路：因为主元素出现的次数大于数组个数的二分之一，则主元素的个数-其它元素的个数 > 0必定成立,根据这个原理对数组进行遍历，先将基数初始化设为数组第一个值，采用一个count值进行计数，当元素等于基数时，count加1,否则count-1.当count == 0时，表明这个数不是当前的主元素，更新基数为当前值，重置count。当遍历完时，必定存在一个数的count大于0,那个数即为主元素。
'''


class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if len(nums) == 0:
            return False
        else:
            count = 1
            curnum = nums[0]
            for i in range(1, len(nums)):
                if curnum == nums[i]:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        curnum = nums[i]
                        count = 1
            return curnum
