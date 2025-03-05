class Solution:
    def coloredCells(self, n: int) -> int:
        """ this should just be a math formula tbh
        1 -> 4
        4 -> 13

        its basically finding the open edges touching other blocks 

        is it legit
        cell_num = 1
        adder = 4
        while n -1 ( because we are doing it n-1 times)
            cell_num += adder
            adder += 4
            n -= 1
        return cell_num"""

        cell_num = 1
        adder = 4
        while n -1:
            cell_num += adder
            adder += 4
            n-=1
        return cell_num
        # O(n) time and O(1) space honestly
