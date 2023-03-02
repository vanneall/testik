def T(matrix: list):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
    return matrix


B = [[0, 2, 1], [1, 0, 3], [0, 1, 1]]
print(T(B))
