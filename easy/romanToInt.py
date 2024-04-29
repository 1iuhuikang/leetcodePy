class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I':1,
            'IV':3,
            'V':5,
            'IX':8,
            'X':10,
            'XL':30,
            'L':50,
            'XC':80,
            'C':100,
            'CD':300,
            'D':500,
            'CM':800,
            'M':1000,
        }
        sum = 0
        for i in range(len(s)):
            current_num = d[s[i]]
            possible_word = s[max(i - 1, 0):i + 1]
            sum += d.get(possible_word, current_num)
        return sum