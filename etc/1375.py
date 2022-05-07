class Solution(object):
    def numTimesAllBlue(self, flips):
        one_count=0
        max_number=0
        count=0
        for i in flips:
            one_count+=1
            if max_number<=i:
                max_number=i
            if max_number==one_count:
                count+=1
        return count
