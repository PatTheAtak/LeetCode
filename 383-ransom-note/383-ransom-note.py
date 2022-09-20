class Solution:
    def canConstruct(self, ransomNote, magazine):
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
