class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create trie for words:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        # dfs/backtracking, start from the top left
        res = set()
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] not in node.children:
                return
            visited.add((r, c))
            char = board[r][c]
            node = node.children[char]
            word += char
            if node.word:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res) 

