"""
Justifies the text so that there are k characters
on each line, with the most words possible, and
so that each word is spaced out as evenly as possible
"""
def justify_text(text, k):
    lines = divide_into_lines(text, k)
    justified = []
    # Takes each line and adds the correct amount of spaces
    # to justify the line
    for line in lines:
        length = 0
        line = line.split()
        for l in line:
            length += len(l)

        # If there is only one word in the line, add spaces to the end
        if len(line) == 1:
            justified.append(line[0] + (" " * (k - length)))
            continue

        # Adds spaces evenly until the length == k
        # Spaces should not be added to the end
        while length < k:
            for i in range(len(line) - 1):
                if length == k:
                    break
                else:
                    line[i] += " "
                    length += 1

        line = "".join(line)
        justified.append(line)

    return justified

def divide_into_lines(text, k):
    lines = []
    current_line = text.pop(0)

    for word in text:
        if len(current_line) + len(word) < k:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

if __name__ == "__main__":
    print(justify_text(["the", "quick", "brown",
                        "fox", "jumps", "over",
                        "the", "lazy", "dog"],
                        k = 16))

    print(justify_text(["the"], k=12))