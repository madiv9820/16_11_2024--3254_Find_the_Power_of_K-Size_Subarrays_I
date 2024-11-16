from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([1,2,3,4,3,2,5], 3, [3,4,-1,-1,-1]),
                            2: ([2,2,2,2,2], 4, [-1,-1]), 
                            3: ([3,2,3,2,3,2], 2, [-1,3,-1,3,-1])}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case1(self):
        nums, k, output = self.__testCases[1]
        result = self.__obj.resultsArray(nums = nums, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case2(self):
        nums, k, output = self.__testCases[2]
        result = self.__obj.resultsArray(nums = nums, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case3(self):
        nums, k, output = self.__testCases[3]
        result = self.__obj.resultsArray(nums = nums, k = k)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

if __name__ == '__main__':
    unittest.main()