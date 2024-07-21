from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * (len(nums))

    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


nums = [1, 2, 4, 6]
print(productExceptSelf(nums))
