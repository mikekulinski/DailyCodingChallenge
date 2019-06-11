def num_paths(num_steps, step_options):
    diff_steps = climb_staircase(num_steps, step_options)
    return len(list(diff_steps))

def climb_staircase(num_steps, step_options, steps_taken = []):
    if num_steps == 0:
        yield steps_taken
    else:
        for s in step_options:
            if (num_steps - s >= 0):
                yield from climb_staircase(num_steps - s,  step_options, steps_taken + [s])


def test1():
    print("Test 1:")
    results = num_paths(4, [1,2])
    assert(results == 5)
    print("PASSED")

def test2():
    print("Test 2:")
    results = num_paths(5, [1, 3, 5])
    assert(results == 5)
    print("PASSED")


if __name__ == "__main__":
    test1()
    test2()