class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Check if strs is empty
        if not strs:
            #returns "" if strs is empty
            return ""
    
        #Start by assuming the entire first string is the common prefix
        prefix = strs[0]
    
        #Compare the prefix with each string in the array
        for string in strs[1:]:
        #Find the common prefix between the prefix so far and the current string
            while string[:len(prefix)] != prefix and prefix:
                #Reduce the prefix by one character at a time
                prefix = prefix[:-1]
            
            #If no common prefix, return an empty string
            if not prefix:
                return ""
    
        return prefix


CODE EXPLANATION:
if not strs:
    return ""

performs the following:

- `if not strs:` checks whether the input list `strs` is empty. In Python, an empty list evaluates to `False` in a boolean context, so `not strs` will be `True` if `strs` is an empty list (i.e., `[]`).
  
- `return ""` immediately returns an empty string `""` if the list `strs` is empty. This ensures that the function doesn't try to process the list when there are no strings to compare.

Why is it needed?
- If `strs` is empty, there are no strings to find a common prefix from, so the function should return an empty string.


The line of code:
while string[:len(prefix)] != prefix and prefix:
    prefix = prefix[:-1]

performs the following actions:

1. `string[:len(prefix)]`:
   - This part extracts a substring from the current string `string`, starting from the first character and ending at the length of the current `prefix`.
   - For example, if `prefix = "fl"` and `string = "flow"`, then `string[:len(prefix)]` would extract `"fl"`.

2. `!= prefix`:
   - This checks if the substring extracted from the current string does not match the current `prefix`. If the current portion of `string` does not match the `prefix`, it means the common prefix between the two strings has to be shortened.

3. `and prefix:`:
   - This ensures that the loop continues only if `prefix` is non-empty. If the `prefix` becomes an empty string, the loop will stop, preventing further processing.

4. `prefix = prefix[:-1]`:
   - This shortens the `prefix` by one character from the end. For example, if `prefix = "flow"`, then `prefix[:-1]` will make it `"flo"`. This process continues until a common prefix is found or the `prefix` becomes an empty string.

What this line does:
It iteratively shortens the `prefix` one character at a time from the end, as long as the current `prefix` doesn't match the corresponding portion of the current string. The goal is to progressively reduce the `prefix` until it becomes the longest common prefix shared by all strings. If no common prefix exists, the loop will reduce `prefix` to an empty string `""`.

Example:
For `strs = ["flower", "flow", "flight"]`:
- Starting with `prefix = "flower"`, the loop will compare it to `"flow"` and shorten it to `"flow"` because that's the longest prefix common between `"flower"` and `"flow"`.
- Next, it compares `"flow"` with `"flight"` and shortens the prefix to `"fl"`, which is the longest prefix common between all three strings.
