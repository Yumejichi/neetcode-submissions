from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        # compare two words each time:
        prev = words[0]
        for word in words[1:]:
            index = 0

            while index < len(prev) and index < len(word):
                if prev[index] != word[index]:
                    graph[prev[index]].add(word[index])
                    break
                index += 1

            if index==min(len(word),len(prev)) and len(prev) > len(word):
                return ""
            prev = word


        indegrees = {letter:0 for letter in graph}

        for letter in graph:
            for neighbor in graph[letter]:
                indegrees[neighbor] += 1
        
        res = []
        q = deque()
        for letter in indegrees:
            if indegrees[letter] == 0:
                q.append(letter)
        
        while q:
            letter = q.popleft()
            res.append(letter)

            for neighbor in graph[letter]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        return "".join(res) if len(res) == len(graph) else ""


