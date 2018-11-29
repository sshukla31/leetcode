"""
Implement Trie
"""

class Node(object):
    def __init__(self, children=None, end_of_word=True):
        self.children = dict() if children is None else children
        self.end_of_word = end_of_word

    def __repr__(self):
        return "{}\n{}".format(
            self.children,
            self.end_of_word
        )


class Trie(object):
    def __init__(self):
        self.root = Node()

    def get_root(self):
        return self.root

    def insert(self, word):
        pointer = self.root
        for char in word:
            if char in pointer.children:
                pointer = pointer.children[char]
            else:
                new_node = Node()
                pointer.children[char] = new_node
                pointer.end_of_word = False
                pointer = new_node


    def is_word_present(self, word):
        pointer = self.root
        for char in word:
            if char in pointer.children and pointer.end_of_word is False:
                pointer = pointer.children[char]
            else:
                return False

        return True

    def is_partial_present(self, partial_word):
        pointer = self.root
        for char in partial_word:
            if char in pointer.children:
                pointer = pointer.children[char]
            else:
                return False

        return True



def main():
    words = [
        "abc",
        "abgl",
        "cdf",
        "abcd",
        "lmn"
    ]
    trie = Trie()
    for word in words:
        trie.insert(word)


    ####################################
    #               TEST CASES        #
    ###################################


    ###################
    # Full word search
    ###################


    # Happy Case: Full word search
    expected_result = [True] * len(words)
    actual_result = [trie.is_word_present(word) for word in words]
    assert expected_result == actual_result

    # Failure Case: Full word search
    expected_result = False
    actual_result = trie.is_word_present("abe")
    assert expected_result == actual_result


    ###################
    # Partial word search
    ###################

    # Happy Case: Partial word search
    partial_words = ["ab", "cd", "l"]
    expected_result = [True] * len(partial_words)
    actual_result = [trie.is_word_present(word) for word in partial_words]
    assert expected_result == actual_result

    # Failure Case: Partial word search
    expected_result = False
    actual_result = trie.is_word_present("xyz")
    assert expected_result == actual_result


if __name__ == '__main__':
    main()