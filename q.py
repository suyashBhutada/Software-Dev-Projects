import bisect
class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        # del original_list[index_to_remove]
        def findClosest(givenList, target):
           return bisect.bisect_left(givenList, target)
        
        tasks.sort()
        num_sessions = 0
        while len(tasks):
            currSTRemaining = sessionTime
            num_sessions += 1
            to_remove_index = findClosest(tasks,currSTRemaining)
            while(to_remove_index):
                if to_remove_index == 0:
                    closest = tasks[0]
                elif to_remove_index == len(tasks)-1:
                    closest = tasks[-1]
                else:
                    closest = tasks[to_remove_index-1]
                currSTRemaining -= closest
                tasks.remove(closest)
                to_remove_index = findClosest(tasks,currSTRemaining)
            
        return num_sessions
# print(Solution().minSessions([1,2,3],3))


from collections import *
from itertools  import *
class ProdPalind:
    def maxProduct(self, s: str) -> int:
        n, d = len(s), defaultdict(int)

        for mask in range(1<<n):                                # <-- 1
            sub = [s[i] for i in range(n) if mask & (1<<i)]     #

            if sub == sub[::-1]: d[mask] = len(sub)             # <-- 2
        print(d)
        return max(d[mask1] * d[mask2] for mask1, mask2         # <-- 3
                    in combinations(d,2) if mask1 & mask2 == 0) 

print(ProdPalind().maxProduct("abc"))


        