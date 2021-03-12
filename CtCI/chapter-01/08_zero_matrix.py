"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""

def zero_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = set()
    col = set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for i in range(n):
        for j in range(m):
            if (i in row) or (j in col):
                matrix[i][j] = 0
    return matrix
