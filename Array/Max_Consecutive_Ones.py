"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
  Input: nums = [1,1,0,1,1,1]
  Output: 3
  Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
  Input: nums = [1,0,1,1,0,1]
  Output: 2
"""

class Solution(object):
  def findMaxConsecutiveOnes(nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      count = 0 # for counting the 1
      max = 0 # for storing the max 1's number
      
      # for every number in the list, if number is 0, then we reset the counting, if number is 1, we increase the count
      for i in nums:
          if i == 0:
              count = 0 
          else:
              count += 1
              # we compare the current count to the "max" count, if it's larger than max, then we replace old max with new one
              if count > max:
                  max = count
                  print("max ", max)
      
      return max

if __name__ == "__main__":
  print(Solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))