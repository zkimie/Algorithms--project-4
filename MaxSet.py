 
#Date: 02/08/24
#Course: Algorithms 325
#Time complexity: 0(n)


def max_independent_set(nums):
    """Returning a list that contains non-consecutive elements that produces
    the maximum sum within that list"""
    n = len(nums) #calculate the length of our list
    if n == 0: #if we are given an empty list, then we return a empty list
        return []

#basecases
    if all(num <= 0 for num in nums): #for all the numbers that are less than or equal to 0
        if 0 in nums: #if there is a 0, we return 0
            return [0]
        return [] #otherwise, they are all negative and we return an empty list per base case

    dp = [0] * n #we're going to store the maximum sum at each position
    subsequence = [[]] * n # and then we have an empty list with the length of our n

    dp[0] = max(0, nums[0]) #we want to calculate the maximum sum of the first elements in the list
    subsequence[0] = [nums[0]] if nums[0] > 0 else [] #if we are going to include this element, checking if the element is greater than 0, otherwise empty list

    for i in range(1, n): #since we already looked at first element at index 0, we iterate through the list
        if nums[i] > 0: #making sure if element is a positive number
            #max sum from previous element compared to max sum of previous to the now current element
            dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i > 1 else 0)) #calculating the max sum and update the subseq.

            if dp[i] == dp[i - 1]: #check if the max sum is the same as the previous one
                subsequence[i] = subsequence[i - 1] #meaning that the current element didnt increase max sum, so should be the same previous subsequent element bc no need to change it

            else:
                subsequence[i] = subsequence[i - 2] + [nums[i]] #otherwise we do add the subsequence from the two elements
        else: #if it is negative or zero
            dp[i] = dp[i - 1] #these two stay the same as the previous element
            subsequence[i] = subsequence[i - 1]

    return subsequence[-1] #return the subsequence which was associated with the last element



# Example tests
nums1 = [-36, -65, 0, -41, -1, 0]
print(max_independent_set(nums1))  # Output: [0]

nums2 = [0, -2, -10, 34, 2, -30]
print(max_independent_set(nums2))  # Output: [0, 34, 2]

# Example tests
nums1 = [-36, -65, 0, -41, -1, 0]
print(max_independent_set(nums1))  # Output: [0]

nums2 = [0, -2, -10, 34, 2, -30]
print(max_independent_set(nums2))  # Output: [0, 34, 2]

# Test cases
nums1 = [-36, -65, 0, -41, -1, 0]
print(max_independent_set(nums1))  # Output: [0]

nums2 = [0, -2, -10, 34, 2, -30]
print(max_independent_set(nums2))  # Output: [0, 34, 2]

nums1 = [7,2,5,8,6]
print(max_independent_set(nums1))

nums2 = [-1, -1, 0]
result2 = max_independent_set(nums2)
print(result2)  # Output: [0]

nums3 = [-1, -1, -10, -34]
result3 = max_independent_set(nums3)
print(result3)  # Output: []

nums10 = [-36,-65,0,-41,-1,0]
print(max_independent_set(nums10))

nums2= [0,-2,-10,34,2,-30]
print(max_independent_set(nums2))
