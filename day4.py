import math


def first_missing(array):
    first_positive = segregate(array)
    pos_array = array[first_positive:]

    # Set the values at the found index negative so
    # we can check later if they had been seen already
    for i in range(len(pos_array)):
        index = abs(pos_array[i]) - 1
        if (index < len(pos_array) and pos_array[index] > 0):
            pos_array[index] = -pos_array[index]

    # Check for first not found value (aka first positive value)
    for i in range(len(pos_array)):
        if (pos_array[i] > 0):
            # i + 1 is the first missing positive value
            return i + 1

    return len(pos_array) + 1


def segregate(array):
    j = 0
    for i in range(len(array)):
        # If value is <= 0, then swap with first positive index
        if (array[i] <= 0):
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            j += 1

    return j


def test1():
    array = [3, 4, -1, 1, -3, 5, -7]
    assert(first_missing(array) == 2)


def test2():
    array = [1, 2, 0]
    assert(first_missing(array) == 3)


def test3():
    array = [-1, 0, -8, -17, -5]
    assert(first_missing(array) == 1)


if __name__ == "__main__":
    test1()
    test2()
    test3()
