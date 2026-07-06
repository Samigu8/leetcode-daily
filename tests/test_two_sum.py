from solutions.two_sum import Solution, two_sum

def test_two_sum_basic():
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
