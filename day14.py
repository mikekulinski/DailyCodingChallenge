import random
import math

def estimatePi():
    in_circle = 0
    total = 10_000_000

    for i in range(total):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if x**2 + y**2 <= 1.0:
            in_circle += 1

    pi = (4 * in_circle) / total
    return pi

def test():
    print("Test:")
    pi = estimatePi()
    epsilon = .001
    print(pi)
    assert(abs(pi - math.pi) <= epsilon)
    print("PASSED")


if __name__ == "__main__":
    test()