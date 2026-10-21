from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Pass 1: Left products
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]

        # Pass 2: Right products (going backwards)
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= (
                right_product  # Multiply existing left product by right product
            )
            right_product *= nums[i]  # Update right product for the next step

        return res
