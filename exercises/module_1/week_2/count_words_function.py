# Write a function for counting words
def count_words(file_path):
    # Read file
    with open(file_path, "r") as f:
        read_content = f.read()

    # Process content
    read_content = read_content.replace("\n", " ")
    read_content = read_content.split()
    read_content = [value.lower() for value in read_content]

    # Dictionary
    result = {}
    for value in read_content:
        result[value] = result.get(value, 0) + 1

    return result


if __name__ == "__main__":
    file_path = "P1_data.txt"
    result = count_words(file_path)
    print(result)
