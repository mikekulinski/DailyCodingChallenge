def longest_k_substring(string, k):
    best = ""
    letters = {}
    substring = ""

    for i in range(len(string)):
        if string[i] not in letters:
            substring += string[i]
            letters[string[i]] = 1
        else:
            substring += string[i]
            letters[string[i]] += 1

        while len(letters) > k:
            front = substring[0]
            substring = substring[1:]
            letters[front] -= 1

            if letters[front] == 0:
                del letters[front]

        if len(letters) == k and len(substring) > len(best):
            best = substring

    return best



def test1():
    print("Test 1:")
    result = longest_k_substring("abcba", 2)
    assert(result == "bcb")
    print("PASSED")

def test2():
    print("Test 2:")
    result = longest_k_substring("abcxyzzzyxyzcbaabcd", 3)
    assert(result == "xyzzzyxyz")
    print("PASSED")


if __name__ == "__main__":
    test1()
    test2()
