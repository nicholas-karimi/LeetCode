# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# 0(n^2) -> runtime -> bruteforce

# sol 1

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         print(f"We're here {i}")
#         for j in range(len(nums)):
#             print(f"Got to j {j}")
#             if nums[i] + nums[j] == target:
#                 print(f"Target {target} is {nums[i] + nums[j]}")
#                 return [i, j]
            
# sol 2 -> use a hashmap
def twoSum(nums, target):
    prevSum = {}
    for i, n in enumerate(nums):
        # print(i, n)
        diff = target - n
        if diff in prevSum:
            return [prevSum[diff], i]
        prevSum[n] = i
    return

twoSum([2, 7, 11, 15], 9) #case1
# twoSum([3,2,4], 6) #case2
# twoSum([3,3], 6) #case3
