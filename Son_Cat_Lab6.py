def find_second_largest(numbers):
    """
    Given a list of numbers, return the second largest one in the list.

    We assume all numbers are positive and that len(numbers) >= 2

    There are TWO bugs in this code.
    """
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or (num > second_largest and num != largest):
            second_largest = num

    return second_largest


def right_triangle(n):
    """
    Recursively print out a right triangle of *'s with n levels. Assume n > 0

    E.g. n = 4 -->  ****
                    ***
                    **
                    *

    There are TWO bugs in this code.
    """
    if n > 0:
        print("*" * n)
        right_triangle(n - 1)


def three_sum(numbers, n):
    """
    Given a list of numbers and a target n, return True if any three of the numbers add up to n and False otherwise.

    This code has TWO bugs (one of them occurs multiple times).
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == n:
                    return True
    return False

# ------- HELPER CODE: DO NOT MODIFY -------

print(find_second_largest([1, 3, 5, 6, 7, 8]))  # Expected output: 7

right_triangle(4)  # Expected output: same as docstring

print(three_sum([5, 6, 7, 8, 9], 4))  # Expected output: False
print(three_sum([5, 6, 7, 8, 9], 21))  # Expected output: True
print(three_sum([5, 6, 7, 8, 9], 15))  # Expected output: False