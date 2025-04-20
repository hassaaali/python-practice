"""
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.

Analysis:
1. Create the given dictionary of pairs
2. Go in revered order in the dictonary and divide each num by value of roman
3. If result has value, append (roman key* result) to result
4. Return the result at end

Time Complexity will be O(1) as the number of iterations are fixed over the dictionary
Space complexity will be O(1) as constant space is used in the dictionary

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        roman_integer = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        for key, value in roman_integer.items():
            if num // value:
                numerals =  num // value
                result += key * numerals
                num = num % value

        return result
# Test Case
num = 3749
test = Solution()
print(test.intToRoman(num))