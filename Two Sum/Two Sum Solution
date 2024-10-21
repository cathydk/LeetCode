class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the value and its index
        num_dict = {}
        
        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and current number
            diff = target - num
            
            # If the difference is already in the dictionary, return the indices
            if diff in num_dict:
                return [num_dict[diff], i]
            
            # Otherwise, store the current number with its index
            num_dict[num] = i  


Code Explanation:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Create a dictionary to store the value and its index
        num_dict = {}


- Dictionary Initialization: 
  - We initialize an empty dictionary `num_dict`. This dictionary will store key-value pairs, where the key is the number in the `nums` array, and the value is the index of that number. 
  - This will help us keep track of numbers we’ve already seen and quickly check if we’ve seen the number that, when added to the current number, equals the target.


        # Loop through the array
        for i, num in enumerate(nums):


- Iterating through the array: 
  - We use the `enumerate(nums)` function to loop through `nums`, which gives us both the index (`i`) and the value (`num`) at each step.
  - For each number in the array, we are going to check if there is another number we’ve already seen that adds up to the `target`.


            # Calculate the difference between the target and current number
            diff = target - num


- Calculate the complement (`diff`): 
  - For each number (`num`), we calculate its complement (`diff`), which is the number we need to find such that `num + diff = target`.
  - This is done by simply subtracting `num` from the `target` (`diff = target - num`).


            # If the difference is already in the dictionary, return the indices
            if diff in num_dict:
                return [num_dict[diff], i]


- Check if the complement (`diff`) exists: 
  - We check if `diff` exists in `num_dict`. If it does, that means we have already seen the number `diff`, and its index is stored in `num_dict[diff]`.
  - Since `num + diff == target`, we can return the indices of `diff` (stored in the dictionary) and `num` (the current index `i`).
  - The function returns a list of the two indices: `[num_dict[diff], i]`.


            # Otherwise, store the current number with its index
            num_dict[num] = i


- Store the current number in the dictionary: 
  - If `diff` is not found in `num_dict`, we add the current `num` and its index `i` to the dictionary. This step ensures that we are storing the numbers we’ve seen so far and can quickly look them up if needed.
  
Example Walkthrough:

Let's walk through an example where `nums = [2, 7, 11, 15]` and `target = 9`.

1. Iteration 1:
   - `i = 0`, `num = 2`
   - `diff = target - num = 9 - 2 = 7`
   - `7` is not in `num_dict` (since the dictionary is empty initially).
   - Add `2` to `num_dict`: `{2: 0}`.

2. Iteration 2:
   - `i = 1`, `num = 7`
   - `diff = target - num = 9 - 7 = 2`
   - `2` is in `num_dict` (from the previous iteration). The index of `2` is `0` (stored in `num_dict[2]`).
   - So, we return `[0, 1]` because `nums[0] + nums[1] = 2 + 7 = 9`.

Time and Space Complexity:
- Time Complexity: O(n), where `n` is the number of elements in `nums`. We only iterate through the list once, and each lookup in the dictionary is O(1) (constant time).
- Space Complexity: O(n), because we store each element of `nums` in the dictionary.

Summary of Key Concepts:
1. Hash Map (Dictionary): Used for fast lookups of previously seen numbers.
2. Complement Calculation: For each number, we calculate the difference between the target and the current number to find the complement we need.
3. Single Pass: We iterate through the array only once, checking for the complement in each step and storing numbers we’ve seen so far.
4. Return Indices: We return the indices of the two numbers whose sum equals the target.

This solution is optimal because it uses only one pass through the array and uses a dictionary for fast lookups.
