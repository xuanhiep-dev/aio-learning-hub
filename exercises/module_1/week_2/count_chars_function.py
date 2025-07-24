# Write a function for counting chars in word
def count_chars(word):
    result = {}
    for value in word:
        result[value] = result.get(value, 0) + 1

    return result


if __name__ == "__main__":
    string = "Happiness"
    result = count_chars(string)
    print(result)
