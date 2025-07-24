import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector**2))

    return len_of_vector


def compute_cosine(v1, v2):
    cos_sim = (np.dot(v1, v2)/(compute_vector_length(v1)
               * compute_vector_length(v2)))

    return cos_sim


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 0, 3, 0])
    result = compute_cosine(x, y)
    print(round(result, 3))
