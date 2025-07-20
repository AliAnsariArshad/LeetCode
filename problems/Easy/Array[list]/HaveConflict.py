from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        evs1 = int(event1[0][:2])
        evend1 = int(event1[1][:2])

        evs2 = int(event2[0][:2])
        evend2 = int(event2[1][:2])

        x = set([y for y in range(evs1, evend1+1)])
        z = set([y for y in range(evs2, evend2+1)])
        common = x.intersection(z)
        if common:
            return True
        else:
            return False





s = Solution()
print(s.haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]))
print(s.haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]))
print(s.haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]))
print(s.haveConflict(event1 =["15:19","17:56"], event2 = ["14:11","20:02"]))