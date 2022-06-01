class Trie:
    class Node:
        def __init__(self, val: str=None):
            self.val = str
            self.children = {}
            self.isEnd = False
        
        def addChild(self, node: 'Node') -> None:
            self.children[node.val] = node
            
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.children: # if node already exists, travel down the tree
                node = node.children[c]
            else:
                node.children[c] = self.Node(c)
                node = node.children[c]
        node.isEnd = True
        return None

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True if node.isEnd else False # only return true if it's a full string

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
