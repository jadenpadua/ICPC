# Given an alphabet in an alien language (26 lowercase letters),
# return true if the words in a list are lexographically sorted
# Idea: Use a comparison method, map each letter from the alien alphabet
# To where it would be in the english dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # First we need to init our ht
        ht = dict()
        index = 0
        # Now we need to map each letter in the dictionary to an indexx
        for i in range(len(order)):
            ht[order[i]] = ht.get(order[i],1) + i 

        # Now after we have our indexed dictionary, we iterate through all the words
        # We are needing to compare, words[i-1], words[i] until end
        for i in range(1,len(words)):
            # Calls comparision method here and checks if char comp value > 0
            # if our comparison value > 0, we know that the index in word[i] is lower,
            # which is bad nad invalidates the alien dictionary
            if self.compare(words[i-1],words[i], ht) > 0:
                return False
        # Retu0rn true after loop ends and all words are checked
        return True
    # Comparison method takes in two words and outputs comparison value
    def compare(self, word1, word2, ht):
        # Two pointers, both start at 0 index of both words
        i = 0
        j = 0
        # need this value to compare, whether it be greater or smaller than 0
        char_compare_value = 0
        # Loop iterates as long as pointers on both words and compare value is 0
        while i < len(word1) and j < len(word2) and char_compare_value == 0:
            # calculate our compare value based on indexes of each char in word
            # if val is neg here we know we can break out b/c that char on same index 
            # of both words come before
            char_compare_value = ht[word1[i]] - ht[word2[j]]
            # Keep going if letters are duplicated in both words as you go along
            i += 1
            j += 1
        # Now if the compare value is still 0, it means thw words have duplicate letters
        # its just the length of one word is longer like "hel" and "hello"
        if char_compare_value == 0:
            # now just return the length of both words, value will be positive and false
            # if word1 length is greater than word2 length
            return len(word1) - len(word2)
        else:
            # else juwst return our comparison value and see if pos or neg
            return char_compare_value
