class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s: str, left: int, right: int):
            if left == 0 and right == 0:
                result.append(s)
                return

            if left > 0:
                backtrack(s + "(", left - 1, right)

            if right > left:
                backtrack(s + ")", left, right - 1)

        backtrack("", n, n)
        return result