from solutions.palindrome_number import Solution

def test_palindrome_positive():
    sol = Solution()
    assert sol.isPalindrome(121) is True
    assert sol.isPalindrome(1221) is True
    assert sol.isPalindrome(5) is True

def test_palindrome_negative():
    sol = Solution()
    assert sol.isPalindrome(-121) is False
    assert sol.isPalindrome(10) is False
    assert sol.isPalindrome(123) is False

def test_palindrome_edge_cases():
    sol = Solution()
    assert sol.isPalindrome(0) is True
    assert sol.isPalindrome(1001) is True
    assert sol.isPalindrome(1000021) is False
