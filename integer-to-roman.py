#leetcode 12: Integer to Roman
#Difficulty: Medium
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
             100,  90,  50,  40,
              10,   9,   5,   4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman = []
        for i in range(len(val)):
            count = num // val[i]
            if count:
                roman.append(syms[i] * count)
                num -= val[i] * count
        return ''.join(roman)
# Time Complexity: O(1) since the number of Roman numeral symbols is fixed
# Space Complexity: O(1) for the output string, which has a maximum length of 15 characters (e.g., 3999 = "MMMCMXCIX")