from collections import deque

class InformationNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = InformationNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = InformationNode()
            curr = curr.children[letter]
        curr.word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        if not word:
            return curr.word
        queue = deque([curr])
        current_index = 0
        for i, letter in enumerate(word):
            if not queue:
                return False
            for _ in range(len(queue)):
                curr = queue.popleft()
                if letter == '.':
                    for child in curr.children:
                            queue.append(curr.children[child])
                else:
                    if letter in curr.children:
                        queue.append(curr.children[letter])
        for node in queue:
            if node.word == True:
                return True
        return False





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)