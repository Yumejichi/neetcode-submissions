from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        available_words = set(wordList)

        q = deque([beginWord])
        changes = 1
        while q:
            changes += 1
            curr_len = len(q)
            for _ in range(curr_len):
                curr_word = q.popleft()
                curr_word_arr = list(curr_word)

                for pos, char in enumerate(curr_word_arr):
                    for i in range(26):
                        # we change to all 26 letters
                        new_char = ord('a') + i
                        curr_word_arr[pos] = chr(new_char)
                        new_word = "".join(curr_word_arr)
                        if new_word in available_words:
                            if new_word == endWord:
                                return changes
                            q.append(new_word)
                            available_words.remove(new_word)
                        curr_word_arr[pos] = char
        return 0





