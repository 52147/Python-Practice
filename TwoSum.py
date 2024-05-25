from typing import List

class Solution:
    # self refers to the instance of the class
    # this allows you to access instance attributes and methods in the class
    # List[int] parameter nums is an integer list
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {} # {} refers to an empty dictionary
        
        for i, num in enumerate(nums):
            complement = target - num
            print(f"Index: {i}, Number: {num}, Complement: {complement}, Num to Index: {num_to_index}")
            if complement in num_to_index:
                return [num_to_index[complement], i] # return a list with 2 elements
            num_to_index[num] = i
        
        return [] # [] means empty list

def test_twoSum():
    solution = Solution()
    
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert solution.twoSum(nums1, target1) == [0, 1]
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    assert solution.twoSum(nums2, target2) == [1, 2]
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    assert solution.twoSum(nums3, target3) == [0, 1]
    
    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    target4 = 8
    assert solution.twoSum(nums4, target4) == [2, 4]
    
    # Test Case 5
    nums5 = [0, -1, 2, -3, 1]
    target5 = -2
    assert solution.twoSum(nums5, target5) == [1, 3]
    
    print("All test cases passed!")

test_twoSum()
