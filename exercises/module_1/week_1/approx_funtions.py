# Write factorial function
def factorial_function(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i

    return result


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result = result + ((-1)**i)*(x**(2*i+1)/factorial_function(2*i+1))

    print(result)


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result = result + ((-1)**i)*(x**(2*i)/factorial_function(2*i))

    print(result)


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result = result + (x**(2*i+1)/factorial_function(2*i+1))

    print(result)


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result = result + (x**(2*i)/factorial_function(2*i))

    print(result)


if __name__ == "__main__":
    approx_sin(x=3.14, n=10)
