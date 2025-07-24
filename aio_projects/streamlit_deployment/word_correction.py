import streamlit as st
import pandas as pd


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
    for i in range(source_len):
        d_matrix[i][0] = i

    for j in range(target_len):
        d_matrix[0][i] = j

    result = None
    for i in range(1, source_len):
        for j in range(1, target_len):
            del_cost = d_matrix[i-1][j] + 1
            ins_cost = d_matrix[i][j-1] + 1
            sub_cost = d_matrix[i-1][j-1] + \
                sub_cost_function(source[i-1], target[j-1])
            d_matrix[i][j] = min(del_cost, ins_cost, sub_cost)

    result = d_matrix[source_len-1][target_len-1]

    return result


def load_vocab(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def main():
    # Streamlit codes
    st.title("Word Correction using Levenshtein Distance")
    vocabs = load_vocab(file_path='data/vocab.txt')
    word = st.text_input('Word:')

    if st.button("Compute"):
        # Compute levenshtein distance
        distances = dict()
        for vocab in vocabs:
            distances[vocab] = levenshtein_function(word, vocab)

        # Sorted by distance
        sorted_distences = dict(
            sorted(distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        st.write(pd.DataFrame({
            'Vocabulary': sorted_distences.keys(),
            'Distances': sorted_distences.values(),
        }))


if __name__ == "__main__":
    main()
