#! /bin/python3

class Solution(object):
    def __init__(self, nums, target):
        self.nums = list()
        self.target = int


    def twoSum(self, nums, target):
            #         looping for first int
            for int_one in range(0, (len(nums)-1)):
                    #         looping for the second int
                for int_two in range((int_one+1), (len(nums)-1)):
                    #         checking if the sum is equal to the target
                    if nums[int_one] + nums[int_two] == target:
                        return [int_one, int_two]
                    else:
                        print("There are no such combination")

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution(nums, target)
    indexes_of_sum = s.twoSum(nums, target)
    if indexes_of_sum == [0, 1]:
        print(True)
    else:
        print(False)
