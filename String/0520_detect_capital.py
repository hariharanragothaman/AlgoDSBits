class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word1 = ''.join(c.upper() for c in word)
        word2 = ''.join(c.lower() for c in word)
        word3 = word.title()

        if word == word1 or word == word2 or word == word3:
            return True
        else:
            return False