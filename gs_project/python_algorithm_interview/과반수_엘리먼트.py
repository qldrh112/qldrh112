from collections import defaultdict

# def f(nums):
#     counts = defaultdict(int)
#     for num in nums:
#         if counts[num] == 0:
#             counts[num] = nums.count(num)
        
#         if counts[num] > len(nums) // 2:
#             return num

def f(nums):
    if not nums:
        return None
    
    if len(nums) == 1:
        return nums[0]

    a = f(nums[:len(nums) // 2])
    b = f(nums[len(nums) // 2:])
    return [b, a][nums.count(a) > len(nums) // 2]


nums = [2, 2, 1, 1, 1, 2, 2]
print(f(nums))

