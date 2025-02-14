# Time Complexity : for all insert/search/startswith functions it's O(n) where n is the length of the given string
# Space Complexity : O(n), where n is the length of the given string
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# tries is a prefix tree, where every node has 2 components - a list of 26 children, one for each small case letter
# and an isend variable marking if this node marks the end of a word
# every character will be stored at an index in the children list of the previous character node
# every index in the children array stores a TrieNode 



class Trie(object):

    # every node in the trie will be of trie node type
    # every node will have 26 children
    # is end represents if the word is ending at that particular node/character

    # class for every node
    class TrieNode():
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

    # intializing root node, with the children list and isend variable
    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            index = ord(c) - ord('a')
            # if there is no further node at that index
            # it means we dont have a node that index => we dont have that character under curr
            if curr.children[index] is None:
                # then we create a node, at the index of char c
                curr.children[index] = self.TrieNode()
            
            # else if already exists, we will go that child character
            curr = curr.children[index]
        
        # after we reach the last character in the given word
        curr.isEnd = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                # this means the node does not exist at the required index
                # and thus the word does not exist
                return False
            curr = curr.children[index]
        
        # at the last index/char of the string
        # at that node - we return the value of isend (True if present, else false)
        return curr.isEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        # current starts with root
        curr = self.root

        # going over the given prefix string
        for i in range(len(prefix)):
            c = prefix[i]
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                # node not present at that index (we do not have the character in the prefix)
                return False
            
            # we move our current to this node
            curr = curr.children[index]
        
        # if we came out of the loop - then it means we had all nodes of the characters in the prefix string
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)