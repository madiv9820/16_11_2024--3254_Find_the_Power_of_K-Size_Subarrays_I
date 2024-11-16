from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Get the length of the nums list
        n = len(nums)
        
        # Initialize the results list with -1, which will hold the final answer
        # The size of the results list is (n - k + 1) because that's the number of sliding windows of size k
        results = [-1] * (n - k + 1)
        
        # Iterate through all possible starting positions for subarrays of size k
        for index in range(n - k + 1):
            # The current subarray is from index to index + k
            start, end = index, index + k
            
            # Assume the subarray is sorted initially
            is_Sorted = True

            # Check if the subarray is sorted in consecutive increasing order
            for currentIndex in range(start, end - 1):
                # If the next element is not consecutive the current element, the subarray isn't sorted
                if nums[currentIndex + 1] != nums[currentIndex] + 1:
                    is_Sorted = False
                    break
            
            # If the subarray is sorted, store the maximum value from this subarray in the results list
            if is_Sorted:
                results[index] = max(nums[start:end])

        # Return the final results array
        return results
    
if __name__ == '__main__':
    nums, k = [2,2,2,2,2], 4
    sol = Solution()
    print(sol.resultsArray(nums = nums, k = k))