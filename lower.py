#! /bin/python3

class Solution(object):
    def __init__(self, upper_str):
        self.upper_str = str

    def toLowerCase(self, upper_str):
        return upper_str.lower()


if __name__ == "__main__":
    upper_str = 'YeeHAAAAA'
    s = Solution(upper_str)
    print(s.toLowerCase(upper_str))
