def v1():
    col1, col2 = [], []
    with open("Dec1.txt", 'r') as f:
        try:
            for line in f:
                [x.append(y) for x, y in zip([col1, col2], line.split())]
                # https://stackoverflow.com/questions/28266586/can-you-append-to-multiple-lists-at-once-in-python
        # EOF
        except ValueError:
            pass

    main(col1, col2)


def v2():
    col1, col2 = [], []
    with open("Dec1.txt", 'r') as f:
        try:
            for line in f:
                l_splt = line.split()
                x, y = l_splt[0], l_splt[1]
                col1.append(y), col2.append(x)
        # EOF
        except IndexError:
            pass
    main(col1, col2)


def main(col1 : list, col2 : list) -> int:
    col1.sort()
    col2.sort()
    sum = 0
    for i in range(len(col1)):
        sum += abs(int(col1[i]) - int(col2[i]))
    print(f"Sum: {sum}")


if __name__ == "__main__":
    import timeit
    # Simpler is better - a list comprehension takes much more time to execute
    # than a simple c-like assignment
    print(timeit.timeit("v1()", setup="from __main__ import v1", number=10))
    print(timeit.timeit("v2()", setup="from __main__ import v2", number=10))
