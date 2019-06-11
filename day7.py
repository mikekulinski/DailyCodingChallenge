code = {
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
    "5": "e",
    "6": "f",
    "7": "g",
    "8": "h",
    "9": "i",
    "10": "j",
    "11": "k",
    "12": "l",
    "13": "m",
    "14": "n",
    "15": "o",
    "16": "p",
    "17": "q",
    "18": "r",
    "19": "s",
    "20": "t",
    "21": "u",
    "22": "v",
    "23": "w",
    "24": "x",
    "25": "y",
    "26": "z"
}

def num_of_decoded(input, decoded = ""):
    if (len(input) < 1):
        yield decoded
    else:
        assert(input[0] in code)
        
        yield from num_of_decoded(input[1:], decoded + code[input[0]])

        if (input[:2] in code):
            yield from num_of_decoded(input[2:], decoded + code[input[:2]])

def test1():
    print("Test 1:")
    possibilities = set(num_of_decoded("111"))
    num = len(possibilities)
    assert(num == 3)
    print("Passed")

def test2():
    print("Test 2:")
    possibilities = set(num_of_decoded("12345"))
    num = len(possibilities)
    assert(num == 3)
    print("Passed")

if __name__ == "__main__":
    test1()
    test2()
