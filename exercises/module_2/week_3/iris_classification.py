from sklearn import datasets
import numpy as np
import math


def create_train_data_iris(data):
    return np.array(data)


def compute_prior_probablity(train_data):
    y_unique = [0, 1]
    prior_probability = np.zeros(len(y_unique))

    prior_column = train_data[:, -1]
    prior_total = len(prior_column)
    prior_probability[0] = len(
        prior_column[np.nonzero(prior_column == y_unique[0])])
    prior_probability[1] = prior_total - prior_probability[0]
    prior_probability /= prior_total

    return prior_probability


def get_mean(data):
    return np.sum(data)/len(data)


def get_variant(data, mean_value):
    return np.sqrt(np.sum((data-mean_value)**2)/len(data))


def normal_fomular(x, mean_value, variant_value):
    result = (1/(variant_value*np.sqrt(2*math.pi))) * \
        (np.exp(-1/2*(((float(x)-mean_value)/variant_value)**2)))

    return result


def prediction_iris(x, train_data, prior_probability):
    y_unique = [0, 1]
    iris_preds = []
    for i in range(len(y_unique)):
        data = train_data[np.nonzero(train_data[:, -1] == y_unique[i])][:, 0]
        mean_value = get_mean(data)
        p = normal_fomular(x, mean_value, get_variant(
            data, mean_value))*prior_probability[i]
        iris_preds.append(p)

    return iris_preds


if __name__ == "__main__":
    data = [[1.4, 0], [1, 0], [1.3, 0], [1.9, 0], [2, 0], [1.8, 0],
            [3, 1], [3.8, 1], [4.1, 1], [3.9, 1], [4.2, 1], [3.4, 1]]
    train_data = create_train_data_iris(data)
    prior_probability = compute_prior_probablity(train_data)
    x = 3.4
    iris_preds = prediction_iris(x, train_data, prior_probability)

    if iris_preds[0] > iris_preds[1]:
        print("Type 0")
    else:
        print("Type 1")
