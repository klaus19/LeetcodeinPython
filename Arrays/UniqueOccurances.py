class Solution(object):
    def uniqueOccurrences(self, arr):

        # Create an empty dictionary to store occurrences as values and numbers as keys
        count_dict = {}

        # Count the occurrences of each number in the array and store in the dictionary
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

                # Create a set to store the unique occurrences
        unique_occurrences = set(count_dict.values())

            # Check if the length of the set is the same as the length of the original dictionary
        return len(unique_occurrences) == len(count_dict)

if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    print(Solution().uniqueOccurrences(arr))