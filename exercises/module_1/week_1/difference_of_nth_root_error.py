import math


# Write different of n root error function
def md_nre_single_sample(y, y_hat, n, p):
    result = (math.pow(y, 1 / n) - math.pow(y_hat, 1 / n))**p
    print(result)


if __name__ == "__main__":
    md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1)
