"""
Rotate Matrix: Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            top = matrix[layer][i]
            # left -> top
            matrix[layer][i] = matrix[-i -1][layer]
            # bottom -> left
            matrix[-i -1][layer] = matrix[-layer -1][-i -1]
            # right -> bottom
            matrix[-layer -1][-i -1] = matrix[i][-layer -1]
            # top -> left
            matrix[i][-layer -1] = top
    return matrix
