# Time Complexity : 
# - inserting dictionary words in the trie - O(mk), where m is the no of words in dict, and k is the avg length of words in dict
# - extracting words from sentences - O(n), n is the no of words in a sentence
# - traversing over every character in a word in the sentence - O(nl), l is the avg length of words in the sentence
# - overall O(mk) + O(nl)
# Space Complexity : O(mk) for the trie and O(nl) for the answer (sentence)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

# Your code here along with comments explaining your approach:
# we put the dictionary words in the trie
# and then traverse over all the words of the sentence
# then we try to match every character of a word in the sentence, with the index of character in the trie
# if we iterate over the trie without any mismatch, and we reach the end of a string in the trie (isend = T)
# then we can replace the word in the sentence with the word in the trie (we will have keep a track of the characters in the word of the trie using a list of characters)
# else, we just append the same word of the sentence in our answer



class Solution(object):

    class TrieNode():
        # every node will have an array of 26 letters as children
        # and every node will have an isend value
        def __init__(self):
            # since we are putting dictionary in the trie - that consists of only lower case letters
            self.children = [None] * 26
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        curr = self.root
        # iterating over all indices of he given word
        for i in range(len(word)):
            c = word[i]
            # to get ascii values
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                # node does not exist, so we add it
                curr.children[index] = self.TrieNode()
            
            # and then move curr to this node
            curr = curr.children[index]
        
        # changing the isend at that node to True, marking the end of this word
        curr.isEnd = True

    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        if dictionary is None or sentence is None:
            return sentence
        
        # inserting every word in trie
        for word in dictionary:
            self.insert(word)
        
        # list of all the words in the sentence
        words = sentence.split()

        # iterate through all the words in the sentence
        # and check if we have a prefix of them in the trie

        
        answer = [] # final sentence

        # iterating over all words in the sentence
        for i in range(len(words)):
            word = words[i]
            sb = [] # list of characters - as a string builder, to store the word from the trie
            # that is to replace the word in the sentence

            # we try to search for all the characters in this word in the trie
            # until we find a prefix (isend = T) without a mismatch
            curr = self.root

            for j in range(len(word)):
                # taking every character from this word
                c = word[j]
                index = ord(c) - ord('a')
                # if there is no node at this index, it means that the prefix does not exist
                # of if we are the end of the word in the dictioary (trie) and we have not exhausted the word in the sentence
                # eg; cat in dict and cattle in word - so we stop at cat (no need to traverse tle)
                # then also we stop
                if curr.children[index] is None or curr.isEnd is True:
                    break
                
                sb.append(c) # appending the matched character
                
                # move current
                curr = curr.children[index]
            
            # if the last node in the Tree is the end 
            if curr.isEnd == True:
                answer.append(''.join(sb))
            else:
                answer.append(word)

        return ' '.join(answer)





        