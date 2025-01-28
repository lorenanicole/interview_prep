# https://leetcode.com/problems/summary-ranges/

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) < 1:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        ranges = [[nums[0]]]
        output = []

        for elem in nums[1:]:
            if elem - ranges[-1][-1] == 1:
                ranges[-1].append(elem)
            else:
                ranges.append([elem])
        
        for range in ranges:
            if len(range) > 1:
                output.append(f'{range[0]}->{range[-1]}')
            else:
                output.append(f'{range[0]}')
        
        return output

solution = Solution()
print(solution.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"])
print(solution.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"])