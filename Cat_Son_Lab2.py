from collections import Counter


def most_frequent_with_tie(lst):
    counts = Counter(lst)

    most_frequency = max(counts.values())

    most_frequent_elements = [element for element, frequency in counts.items() if frequency == most_frequency]

    return min(most_frequent_elements)

def longest_sequence_length(lst):
    current_length = 1
    max_length = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)

user_input = input("Enter a list of integers separated by spaces: ")

user_list = list(map(int, user_input.split()))

result1 = most_frequent_with_tie(user_list)
result2 = longest_sequence_length(user_list)
print("The most frequent element with the smallest value is:", result1)
print("longest_sequence_length:", result2)