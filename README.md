# Finding the power of K-Size subarrays using Sliding Window Approach

- ### Problem Explanation
    You are given an array `nums` of integers of length `n` and a positive integer `k`. You need to find the "power" of every subarray of size `k` in the array.

    The **power** of a subarray is defined as:

    - **The maximum element of the subarray** if all its elements are **consecutive and sorted in ascending order**.
    - **-1** otherwise, i.e., if the elements are not consecutive and sorted in ascending order.

    Your task is to return an integer array `results` of size `(n - k + 1)`, where `results[i]` is the power of the subarray `nums[i..(i + k - 1)]`.

- ### Key Concepts
    1. **Consecutive and Sorted**: A subarray is considered sorted and consecutive if each element in the subarray is one greater than the previous element. For example, `[1, 2, 3]` is sorted and consecutive, but `[3, 4, 2]` is not.
    2. **Sliding Window**: You need to examine every contiguous subarray of size `k` in the given array. This can be efficiently done using a sliding window approach.
    3. **Power Calculation**: For each valid subarray (consecutive and sorted), return the maximum element. For invalid subarrays (not consecutive or not sorted), return `-1`.

- ### Approach
    1. **Sliding Window**:
    - Use a sliding window of size `k` to iterate through all subarrays of size `k`. The window slides from index `0` to `n - k`, where `n` is the length of the input array `nums`.
    2. **Check for Sorted and Consecutive**:
    - For each subarray of size `k`, check if the elements are sorted in consecutive order. This can be done by iterating through the subarray and verifying that each element is exactly one greater than the previous element (`nums[i + 1] == nums[i] + 1`).
    3. **Find Maximum**:
        - If the subarray is sorted and consecutive, find the maximum element using `max()`.
        - If the subarray is not sorted or consecutive, store `-1` for that subarray.

    4. **Return Result**:
        - The final result is an array where each element corresponds to the "power" of the subarray starting at that index.

- ### Code
    - **Python Solution**

        ```python3 []
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
        ```

    - **C++ Solution**

        ```cpp []
        class Solution {
        public:
            vector<int> resultsArray(vector<int>& nums, int k) {
                // Get the size of the input vector nums
                int n = nums.size();
                
                // Initialize the results vector with -1 values, with size (n - k + 1)
                // This represents the number of subarrays of size k
                vector<int> results(n - k + 1, -1);

                // Iterate through all possible starting positions for subarrays of size k
                for (int index = 0; index <= n - k; ++index) {
                    // Set the current subarray's start and end indices
                    int start = index, end = index + k;
                    
                    // Flag to check if the subarray is sorted (consecutive integers)
                    bool is_Sorted = true;
                    
                    // Check if the subarray nums[start:end] is sorted with consecutive integers
                    for (int currentIndex = start; currentIndex < end - 1; ++currentIndex) {
                        // If the next element is not consecutive the current element, the subarray isn't sorted
                        if (nums[currentIndex + 1] != nums[currentIndex] + 1) {
                            is_Sorted = false;
                            break; // Exit the loop as we found that the subarray isn't sorted
                        }
                    }

                    // If the subarray is sorted, store the maximum value from this subarray in the results vector
                    if (is_Sorted)
                        results[index] = *max_element(nums.begin() + start, nums.begin() + end);
                }

                // Return the results vector
                return results;
            }
        };
        ```

- ### Time Complexity
    1. **Outer Loop**:
        - The outer loop iterates over each possible starting index for a subarray of size `k`. The number of such subarrays is `(n - k + 1)`, so the loop runs `O(n - k + 1)` times, which simplifies to `O(n)`.
    2. **Inner Loop**:
        - For each subarray, we need to check if the elements are consecutive and sorted. This takes `O(k)` time for each subarray, as we need to verify `k - 1` pairs of adjacent elements.
    3. **Finding Maximum**:
        - Finding the maximum value of each subarray of size `k` takes `O(k)` time.

    Thus, the total time complexity is: O(n * k), where `n` is the length of the array and `k` is the size of the subarray.

- ### Space Complexity
    1. **Result Array**:
        - We need an array `results` of size `n - k + 1` to store the result, which requires `O(n)` space.
    2. **Auxiliary Variables**:
        - We use only a few auxiliary variables to keep track of the indices and a flag to check if a subarray is sorted, which require constant space (`O(1)`).

    Thus, the total space complexity is: O(n), since the dominant space usage is from the `results` array.