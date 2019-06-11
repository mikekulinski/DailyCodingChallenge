class Trie:
    def __init__(self, letter, is_end):
        self.letter = letter
        self.children = set()
        self.is_end = is_end

    def addWord(self, word):
        if (len(word) < 2):
            is_end = True
        else:
            is_end = False
        
        letter_in_children = False
        for child in self.children:
            if child.letter == word[0]:
                child.addWord(word[1:])
                letter_in_children = True
                return

        if not letter_in_children:
            node = Trie(word[0], is_end)
            self.children.add(node)
            
            if not is_end:
                node.addWord(word[1:])

    def printTrie(self):
        print(self.letter)
        for child in self.children:
            child.printTrie()


def getPrefixTrie(dictionary, prefix):
    trie = Trie(None, False)
    for word in dictionary:
        trie.addWord(word)

    for i in range(len(prefix)):
        for c in trie.children:
            if c.letter == prefix[i]:
                trie = c
                break

    # trie now equals the part of the tree that we should autocomplete
    return set(autocomplete(trie, prefix))

def autocomplete(trie, prefix):
    if trie.is_end:
        yield prefix

    for c in trie.children:
        yield from autocomplete(c, prefix + c.letter)


def test1():
    print("Test 1:")
    results = getPrefixTrie(["dog", "deer", "deal"], "de")
    assert(results == {"deer", "deal"})
    print("PASSED")

def test2():
    print("Test 2:")
    results = getPrefixTrie(["dear", "deer", "dictionary", "plastic", "health", "ear infection", "hello world", "hi"], "h")
    assert(results == {"hi", "hello world", "health"})
    print("PASSED")

if __name__ == "__main__":
    test1()
    test2()