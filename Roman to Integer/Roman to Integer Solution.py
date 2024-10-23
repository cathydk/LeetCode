class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Hold integer value of roman numeral
        integer_value = 0
        #Symbols and its correlating value
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        #Handling the special cases first
        #Roman numeral removed from the string using s.replace(), so they don't get double-counted in the loop
        if "IV" in s:
            integer_value += 4
            s = s.replace("IV", "")
        if "IX" in s:
            integer_value += 9
            s = s.replace("IX", "")
        if "XL" in s:
            integer_value += 40
            s = s.replace("XL", "")
        if "XC" in s:
            integer_value += 90
            s = s.replace("XC", "")
        if "CD" in s:
            integer_value += 400
            s = s.replace("CD", "")
        if "CM" in s:
            integer_value += 900
            s = s.replace("CM", "")
        
        #Handle the remaining characters
        #Loop through string
        #Add to integer_value according to value associated with symbol
        for character in s:
            if character == "I":
                integer_value += I
            if character == "V":
                integer_value += V
            if character == "X":
                integer_value += X
            if character == "L":
                integer_value += L
            if character == "C":
                integer_value += C
            if character == "D":
                integer_value += D
            if character == "M":
                integer_value += M
        
        return integer_value
