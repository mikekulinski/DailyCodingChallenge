def reconstruct_sentence(dictionary, string):
    sentence = []
    current_word = ""
    while string or current_word:
        if current_word in dictionary:
            sentence.append(current_word)
            current_word = ""
        elif len(string) == 0:
            string = current_word + string
            current_word = sentence.pop(-1)
            current_word += string[0]
            string = string[1:]
        else:
            current_word += string[0]
            string = string[1:]

    return sentence

if __name__ == "__main__":
    print(reconstruct_sentence({'bed', 'bath', 'bedbath', 'and', 'beyond'},
                                'bedbathandbeyond'))
    print(reconstruct_sentence({'quick', 'brown', 'the', 'fox'},
                                'thequickbrownfox'))

    print(reconstruct_sentence({'boys', 'them', 'the', 'we'},
                                'wethemboys'))