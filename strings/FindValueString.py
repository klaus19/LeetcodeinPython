class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0

        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                x += 1
            elif operations[i] == "--X" or operations[i] == "X--":
                x -= 1
        return x
if __name__ == "__main__":
    operations = ["--X", "X++", "X++"]
    print(Solution().finalValueAfterOperations(operations))