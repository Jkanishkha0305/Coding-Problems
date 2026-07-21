"""
Contains Duplicate (Easy)
https://leetcode.com/problems/contains-duplicate/

Approach: track seen values in a set; if a value repeats, return True.
Time: O(n), Space: O(n).
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def _test():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("contains_duplicate: all tests passed")


if __name__ == "__main__":
    _test()
