class TrieNode:
    def __init__(self):
        self.children = {}  # a dictionary that maps characters to child TrieNodes
        self.word = False  # a flag indicating whether the node represents the end of a word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # initialize the root node of the Trie

    def addWord(self, word: str) -> None:
        cur = self.root  # start at the root node of the Trie
        for c in word:
            if c not in cur.children:  # if the current character is not a child of the current node
                cur.children[c] = TrieNode()  # create a new child node for the character
            cur = cur.children[c]  # move to the child node for the character
        cur.word = True  # mark the final node as representing the end of a word

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root  # start at the given root node
            for i in range(j, len(word)):  # iterate over each character of the word from the given index
                c = word[i]
                if c == ".":  # if the character is a wildcard character
                    for child in cur.children.values():  # search all child nodes
                        if dfs(i + 1, child):  # if any search returns True
                            return True
                    return False  # if no search returns True, return False
                else:  # if the character is not a wildcard character
                    if c not in cur.children:  # if the character is not a child of the current node
                        return False  # the word is not in the Trie
                    cur = cur.children[c]  # move to the child node for the character
            return cur.word  # return whether the final node represents the end of a word
        return dfs(0, self.root)  # start the DFS from the root node of the Trie and return the result

