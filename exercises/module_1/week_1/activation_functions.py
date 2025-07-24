import math


# Write sigmoid function
def sigmoid_function(x):
    result = 1 / (1 + math.exp(-x))
    return result


# Write relu function
def relu_function(x):
    result = 0
    if x > 0:
        result = x

    return result


# Write elu function
def elu_function(x):
    result = 0
    alpha = 0.01
    if x > 0:
        result = x
    else:
        result = alpha * (math.exp(x) - 1)

    return result


def is_number(n):
    # Type-casting the string to 'float'.
    # If string is not a valid 'float',
    # It'll raise 'ValueError' exception
    try:
        float(n)
    except ValueError:
        return False
    return True


# Write a function with 3 activation functions
def activation_functions():
    # Input x
    x = input("Input x =")
    if is_number(x):
        # Input activation type
        activation_type = input("Input activation function (sigmoid|relu|elu):")
        x = float(x)
        if activation_type == "sigmoid":
            result = sigmoid_function(x)
            print(f"f({x}) = {result}")
        elif activation_type == "relu":
            result = relu_function(x)
            print(f"f({x}) = {result}")
        elif activation_type == "elu":
            result = elu_function(x)
            print(f"f({x}) = {result}")
        else:
            print(f"{activation_type} is not supported")
    else:
        print("x must be a number")


if __name__ == "__main__":
    activation_functions()
