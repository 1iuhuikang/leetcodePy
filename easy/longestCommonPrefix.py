class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = None
        for s in strs:
            if prefix is None or len(s) < len(prefix):
                prefix = s

        for s in strs:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]

        return prefix