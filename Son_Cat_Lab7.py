file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    index = -1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            index = mid
            print(f'Target = {target}, Found at index = {index}, Number of iterations = {iterations}')
            return iterations, index
    print(f'Target = {target}, Found at index = {index}, Number of iterations = {iterations}')
    return -1, iterations
target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()