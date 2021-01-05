from itertools import chain, combinations
import time
import sys

def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return
    first = collection[0]
    for smaller_set in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller_set):
            yield smaller_set[:n] + [[first] + subset] + smaller_set[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller_set


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Incorrect arguments")
        exit(1)
    board = sys.argv[1]
    if not board.isdigit():
        print("Enter the number > 0, number belongs Ν")
    input_set = list(range(1, int(board) + 1))
    print("Все разбиения множества:")
    for n, p in enumerate(partition(input_set), 1):
        print(f"{n}. {{{'},{'.join((','.join([str(i) for i in x]) for x in sorted(p)))}}}")
