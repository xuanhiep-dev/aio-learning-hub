def del_cost_function():
    return 1


def ins_cost_function():
    return 1


def sub_cost_function(source_char, target_char):
    result = 1
    if source_char == target_char:
        result = 0

    return result


# Write a function for counting words
def levenshtein_function(source, target):
    source = "#" + source
    target = "#" + target
    source_len = len(source)
    target_len = len(target)

    # Write matrix D
    d_matrix = [[0]*target_len for _ in range(source_len)]
    for i in range(1, source_len):
        d_matrix[i][0] = d_matrix[i-1][0] + del_cost_function()

    for i in range(1, target_len):
        d_matrix[0][i] = d_matrix[0][i-1] + ins_cost_function()

    result = None
    for i in range(1, source_len):
        for j in range(1, target_len):
            del_cost = d_matrix[i-1][j] + del_cost_function()
            ins_cost = d_matrix[i][j-1] + ins_cost_function()
            sub_cost = d_matrix[i-1][j-1] + \
                sub_cost_function(source[i-1], target[j-1])
            d_matrix[i][j] = min(del_cost, ins_cost, sub_cost)

    result = d_matrix[source_len-1][target_len-1]

    return result


if __name__ == "__main__":
    source = "yu"
    target = "you"

    result = levenshtein_function(source, target)
    print(
        f"Source: {source}, Target: {target}, levenshtein distance: {result}")
