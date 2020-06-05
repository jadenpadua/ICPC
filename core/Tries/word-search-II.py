class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for l in word:
            node = node.children['o']
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for l in word:
            node = node.children.get(l)
            if not node:
                return False
        return node.isWord
        
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board,node,i,j,"",res)
        
        return res
    
    
    def dfs(self,board,node,i,j,path,res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        pointer = board[i][j]
        node = node.children.get(pointer)
        
        if not node:
            return
        
        board[i][j] = "*"
        self.dfs(board,node,i+1,j,path+pointer,res)
        self.dfs(board,node,i-1,j,path+pointer,res)
        self.dfs(board,node,i,j-1,path+pointer,res)
        self.dfs(board,node,i,j+1,path+pointer,res)
        board[i][j] = pointer
    
    
    
    
