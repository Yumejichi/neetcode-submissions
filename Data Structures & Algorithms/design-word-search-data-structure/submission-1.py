class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(curr, index):
            if index == len(word):
                if curr.end:
                    return True
                return False

            if word[index] == ".":
                for c in curr.children.values():
                    res = dfs(c, index+1)
                    if res:
                        return True
                return False
            else:
                if word[index] not in curr.children:
                    return False
                return dfs(curr.children[word[index]], index+1)
            
        return dfs(self.root, 0)

        
