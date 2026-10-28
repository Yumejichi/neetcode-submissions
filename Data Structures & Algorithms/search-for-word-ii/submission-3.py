class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words:
            return []

        res = set()
        visited = set()

        def dfs(curr, r, c): #curr - > Trienode, path -> string 
            if curr.end:
                res.add(curr.word)
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            visited.add((r,c))
            for dr, dc in directions:
                x = r+dr
                y = c + dc
                if 0<=x < len(board) and 0<=y < len(board[0]) and (x,y) not in visited and board[x][y] in curr.children:
                    dfs(curr.children[board[x][y]], x, y)
            visited.remove((r,c))


        trie = Trie()
        for word in words:
            trie.addWord(word)
        for r in range(len(board)):
            for c in range(len(board[0])):
                for children in trie.root.children:
                    if children == board[r][c]:
                        dfs(trie.root.children[children], r, c)

        return list(res)





