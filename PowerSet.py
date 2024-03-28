#course: Algorithms 325
#date: 02/08/2024
#Time complexity: O(2^n)


def powerset(inputSet):
    """ creates a list that shows the powerset of our given inputset, which also includes our
      given input set as well as the empty set"""

    powersets = [] #we create the empty list that will store the subsets

    def backtrack(start, current_subset):
        """obtains two arguments where we have the start (which is the current position) and the
        current subset which is the list that represents the subset being constructed"""
        powersets.append(current_subset[:]) # so we can save a copy of the current sets

#for all the possible combinations(included and excluded)
        for i in range(start, len(inputSet)): #starting from the start index and going to the length of our input set
            current_subset.append(inputSet[i]) #every time we go through the loop, we include the element into subset
            backtrack(i + 1, current_subset) # recursively explore each possibility with the current element
            current_subset.pop() #to back track, we have to exlcude our current element so we pop it off.


    backtrack(0, []) #our recursive call
    return powersets


inputSet1 = [1, 2, 3]
result1 = powerset(inputSet1)
print(result1)  # Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

inputSet2 = []
result2 = powerset(inputSet2)
print(result2)  # Output: [[]]
