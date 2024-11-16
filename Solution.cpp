#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

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

int main() {
    int input, k; vector<int> nums;
    cin >> input;

    while(input != -1) {nums.emplace_back(input); cin >> input;}
    cin >> k;

    Solution sol;
    vector<int> results = sol.resultsArray(nums, k);
    
    for(const int& x: results) cout << x << " ";
    cout << endl;
}