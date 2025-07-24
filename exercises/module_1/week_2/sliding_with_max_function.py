# Write a function for finding max when sliding
def sliding_with_max_function(num_list, k):
    result = []
    length = len(num_list)
    for i in range(length):
        small_list = num_list[i:(i+k)]
        if len(small_list) == k:
            result.append(max(small_list))

    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    result = sliding_with_max_function(num_list, k)
    print(f"Output: {result}")
