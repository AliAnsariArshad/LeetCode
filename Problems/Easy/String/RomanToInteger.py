class Solution:
    def roman_to_integer(self, s: str):
        int_num = 0
        roman_ditc = {"I": 1, 
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000
                      }
        for char in range(len(s)-1):
            if roman_ditc[s[char]] < roman_ditc[s[char+1]]:
                int_num = int_num - roman_ditc[s[char]]
            else:
                int_num = int_num + roman_ditc[s[char]]

        return int_num+roman_ditc[s[-1]]

    def roman_to_int_2(self, s: str):

        roman_ditc = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000
                      }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").\
            replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").\
            replace("CM", "DCCCC")
        return sum(map(lambda x: roman_ditc[x], s))

    def roman_to_int_3(self, s: str):

        roman_ditc = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000
                      }
        s = s.replace("IV", "IIII").replace("IX", "VIIII"). \
            replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC"). \
            replace("CM", "DCCCC")
        sum = 0

        for char in s:
            sum = sum + roman_ditc[char]
        return sum

s = Solution()
print(s.roman_to_integer("MCMXCIV"))
print(s.roman_to_int_2("MCMXCIV"))
print(s.roman_to_int_3("MCMXCIV"))