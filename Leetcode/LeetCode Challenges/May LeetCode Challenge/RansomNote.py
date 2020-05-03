class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Approach 1: Using sorting
        # Sort both of them and use two pointers each at the start of both the strings
        # compare the magazine value with ransom value if both are equal increment both pointer
        #else increment magazine pointer
        if ransomNote == "" :
            return True
        ransomNote,magazine = sorted(ransomNote),sorted(magazine)
        rindex,mindex=0,0
        while mindex<len(magazine):
            if magazine[mindex] == ransomNote[rindex]:
                mindex += 1
                rindex += 1
            else:
                mindex += 1
            if rindex == len(ransomNote):
                return True
        return False
        # Approach 2:using dictionaries
        # for each (key,value) in ransomNote checking if it is less than Magazine

        magazineDct = collections.Counter(magazine)
        ransomDct = collections.Counter(ransomNote)

        for char, count in ransomDct.items():
            if magazineDct[char] < count:
                return False
        return True
s = Solution()
print(s.canConstruct("aa","aab"))