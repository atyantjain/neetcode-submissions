class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for i in strs:
            if str(sorted(i)) in dictionary:
                dictionary[str(sorted(i))].append(i)
            else:
                dictionary[str(sorted(i))]=[i]
        return list(dictionary.values())