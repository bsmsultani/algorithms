"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


"""

def twoSum(nums: list, target: list):

    prevMap = {} # val : index

    # go through the array
    for i, val in enumerate(nums):
        
        # get the desired number to add to target
        diff = target - val

        # if the desired number is in hash map then return its index as wells as the index of the current number
        if diff in prevMap:
            return [prevMap[diff], i]
        
        
        # if the desired number is not in the list
        # add val : index of the current number to the list
          
        prevMap[val] = i

# in the first iteration it will add the first value : index
# second iteration, it will check if the desired value is the first value, if it is then it will return
# the index of the first value \val : index RETURN\, and the index of the second value \i = [1]\ so [0, 1]

# looking for values in a hashmap has a time complexity of O(1)
# and going through the entire array has a time complexity of O(n)
# therefore, this algorithm has a time complexity of O(n)

