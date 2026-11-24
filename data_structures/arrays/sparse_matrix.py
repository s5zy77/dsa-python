def to_triplet(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    triplet = [[rows, cols, 0]]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                triplet.append([i, j, matrix[i][j]])
                count += 1

    triplet[0][2] = count
    return triplet


def transpose_triplet(triplet):
    rows, cols, non_zeros = triplet[0]
    transposed = [[cols, rows, non_zeros]]

    for col in range(cols):
        for k in range(1, non_zeros + 1):
            if triplet[k][1] == col:
                transposed.append([triplet[k][1], triplet[k][0], triplet[k][2]])

    return transposed


if __name__ == "__main__":
    mat = [
        [0, 0, 3, 0],
        [0, 0, 0, 5],
        [7, 0, 0, 0],
    ]
    t = to_triplet(mat)
    print("Triplet Representation (Row, Col, Val):")
    for row in t:
        print(row)

    print("\nTransposed Triplet:")
    for row in transpose_triplet(t):
        print(row)