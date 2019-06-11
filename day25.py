def regex_matching(string, regex):
    i = 0
    j = 0
    while i < len(string) and j < len(regex):
        if string[i] == regex[j]:
            pass
        elif regex[j] == ".":
            return True
        elif regex[j] == "*":
            j -= 1
        else:
            return False
        return True

if __name__ == "__main__":
    print(regex_matching("catss", "cat.*"))