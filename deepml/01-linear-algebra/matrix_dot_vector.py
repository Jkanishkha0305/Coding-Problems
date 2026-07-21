"""
Matrix-Vector Dot Product (Easy)
https://www.deep-ml.com/problems/1

Approach: for each row of the matrix, take the dot product with the vector.
Valid only if the matrix's column count equals the vector's length, else -1.
Time: O(n*m), Space: O(n).
"""


def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    if any(len(row) != len(b) for row in a):
        return -1
    return [sum(x * y for x, y in zip(row, b)) for row in a]


def _test():
    assert matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]) == [14, 25, 49]
    assert matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]) == -1
    assert matrix_dot_vector([[1, 2], [2, 4]], [1, 2]) == [5, 10]
    print("matrix_dot_vector: all tests passed")


if __name__ == "__main__":
    _test()
