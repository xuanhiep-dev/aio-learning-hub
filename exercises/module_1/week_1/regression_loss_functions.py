import random
import math


# Write a sample function
def one_sample_function(predict, target, loss_name):
    result = 0
    if loss_name == "MAE":
        result = abs(predict - target)
    elif loss_name == "MSE" or loss_name == "RMSE":
        result = (predict - target)**2
    else:
        return result

    return result


# Write loss function
def loss_function(n, losses, loss_name):
    result = 0
    if loss_name == "MAE" or loss_name == "MSE":
        result = losses / n
    elif loss_name == "RMSE":
        result = math.sqrt(losses / n)
    else:
        return result

    return result


# Write a function with many regression loss functions
def regression_loss_functions():
    # Input number of samples
    n = input("Input number of samples (integer number) which are generated:")
    if n.isnumeric():
        # Input activation type
        loss_name = input("Input loss name:")
        losses = 0
        n = int(n)
        for i in range(n):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)

            loss = one_sample_function(predict, target, loss_name)
            print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")
            losses += loss

        final_loss = loss_function(n, losses, loss_name)
        print(f"final RMSE: {final_loss}")

    else:
        print("number of samples must be an integer number")


if __name__ == "__main__":
    regression_loss_functions()
