def run_length_encode(string):
    encoded = []
    temp = []
    for c in string:
        if temp == [] or c == temp[-1]:
            temp.append(c)
        else:
            encoded.append(str(len(temp)) + temp[0])
            temp = [c]

    encoded.append(str(len(temp)) + temp[0])
    return "".join(encoded)

        

def run_length_decode(string):
    decoded = []
    num = 0
    for c in string:
        try:
            num = int(c)
        except:
            decoded.append(c * num)
            num = 0

    return "".join(decoded)



if __name__ == "__main__":
    string = "AAAABBBCCDAA"
    encoded = run_length_encode(string)
    decoded = run_length_decode(encoded)
    print(string == decoded)
