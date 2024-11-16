# [3254. Find the Power of K-Size Subarrays I](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i)

__Type:__ Medium <br>
__Topics:__ Sliding Window, Array <br>
__Companies:__ Bloomberg
<hr>

You are given an array of integers `nums` of length `n` and a positive integer `k`.

The __power__ of an array is defined as:

- Its __maximum__ element if _all_ of its elements are __consecutive__ and __sorted__ in __ascending__ order.
- -1 otherwise.

You need to find the __power__ of all subarrays of `nums` of size `k`.

Return an integer array `results` of size `n - k + 1`, where `results[i]` is the _power_ of `nums[i..(i + k - 1)]`.
<hr>

### Examples:
- __Example 1:__ <br>
__Input:__ nums = [1,2,3,4,3,2,5], k = 3 <br>
__Output:__ [3,4,-1,-1,-1] <br>
__Explanation:__ <br>
There are 5 subarrays of nums of size 3:
    - [1, 2, 3] with the maximum element 3.
    - [2, 3, 4] with the maximum element 4.
    - [3, 4, 3] whose elements are not consecutive.
    - [4, 3, 2] whose elements are not sorted.
    - [3, 2, 5] whose elements are not consecutive.

- __Example 2:__ <br>
__Input:__ nums = [2,2,2,2,2], k = 4 <br>
__Output:__ [-1,-1]

- __Example 3:__ <br>
__Input:__ nums = [3,2,3,2,3,2], k = 2 <br>
__Output:__ [-1,3,-1,3,-1]
<hr>

### Constraints:
- `1 <= n == nums.length <= 500`
- <code>1 <= nums[i] <= 10<sup>5</sup></code>
- `1 <= k <= n`
<hr>

### Hints:
- Can we use a brute force solution with nested loops and HashSet?