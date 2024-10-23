class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #Variable to check if palindrome is found or
        is_palindrome = False
        #Convert x to a string to traverse the number
        x_string = str(x) 
        #To hold the reverse value
        #Create a slice that starts at the end of the string, and moves backwards
        #The slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards
        reverse_string = x_string [::-1]
        #Check if it is a palindrome
        if x_string == reverse_string:
            is_palindrome = True
            return is_palindrome
        else:
            return is_palindrome
