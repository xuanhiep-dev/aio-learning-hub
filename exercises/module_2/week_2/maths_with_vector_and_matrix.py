import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector**2))

    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)

    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)

    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)

    return result


def inverse_matrix(matrix):
    result = None
    det_matrix = np.linalg.det(matrix)

    if det_matrix != 0:
        result = np.linalg.inv(matrix)
    else:
        print("No inverse matrix")

    return result


if __name__ == "__main__":
    # 1. Length of a vector
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length(vector)
    # print(round(result, 2))

    # 2. Dot product
    v1 = np.array([0, 1, -1, 2])
    v2 = np.array([2, 5, 1, 0])
    result = compute_dot_product(v1, v2)
    # print(round(result, 2))

    # 3. Multiplying a vector by a matrix
    m = np.array([[-1, 1, 1],
                  [0, -4, 9]])
    v = np.array([0, 2, 1])
    result = matrix_multi_vector(m, v)
    # print(result)

    # 4. Multiplying a matrix by a matrix
    m1 = np.array([[0, 1, 2],
                   [2, -3, 1]])
    m2 = np.array([[1, -3],
                   [6, 1],
                   [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    # print(result)

    # 5. Matrix inverse
    m1 = np.array([[-2, 6],
                   [8, -4]])
    result = inverse_matrix(m1)
    print(result)
