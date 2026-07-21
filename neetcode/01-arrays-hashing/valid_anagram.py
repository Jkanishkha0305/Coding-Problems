"""
Valid Anagram (Easy)
https://leetcode.com/problems/valid-anagram/

Approach: anagrams have identical character-frequency counts.
Compare Counter(s) == Counter(t) (also handles length mismatch implicitly).
Time: O(n), Space: O(n).
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


def _test():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    print("valid_anagram: all tests passed")


if __name__ == "__main__":
    _test()
