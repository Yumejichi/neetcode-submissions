class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True        

    def search(self, word: str) -> bool:
        
        def dfs_search(substring, node):
            for i in range(len(substring)):
                char = substring[i]
                if char == ".":
                    for child_node in node.children.values():
                        if child_node:
                            if dfs_search(substring[i+1:], child_node):
                                return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.word
        return dfs_search(word, self.root)

