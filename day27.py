def well_formed_brackets(string):
    current = ""
    opening = ["(", "{", "["]
    for c in string:
        print(current)

        if c in opening:
            current += c
        elif c == ")":
            if current[-1] == "(":
                current = current[:-1]
            else:
                return False
        elif c == "}":
            if current[-1] == "{":
                current = current[:-1]
            else:
                return False
        elif c == "]":
            if current[-1] == "[":
                current = current[:-1]
            else:
                return False


    if current:
        return False
    else:
        return True


if __name__ == "__main__":
    print(well_formed_brackets("([])[]({})"))
    print(well_formed_brackets("([)]"))
    print(well_formed_brackets("((()"))