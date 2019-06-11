"""
You are given an array of non-negative integers that represents a two-dimensional
elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run
off to the left), so we can trap 8 units of water.
"""


def trapped_rainfall(map, water_amount=0):
    if len(map) < 2:
        return water_amount
    else:
        left = map[0]
        right = map[-1]
        if left <= right:
            index = 1
            while map[index] < left:
                water_amount += left - map[index]
                index += 1
            return trapped_rainfall(map[index:], water_amount)

        else:
            index = -2
            while map[index] < right:
                water_amount += right - map[index]
                index -= 1
            return trapped_rainfall(map[:index], water_amount)


if __name__ == "__main__":
    rainfall1 = trapped_rainfall([3, 0, 1, 3, 0, 5])
    assert rainfall1 == 8

    rainfall2 = trapped_rainfall([1, 4, 7, 2, 9, 5, 1])
    assert rainfall2 == 5
