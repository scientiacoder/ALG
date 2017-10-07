# -*- coding:utf-8 -*-
# __author__=''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        while num > 1:
            if num%2 == 0:
                num=num/2
            elif num%3 == 0:
                num=num/3
            elif num%5 == 0:
                num=num/5
            else:
                return False
        if num == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    print (a.isUgly(0))