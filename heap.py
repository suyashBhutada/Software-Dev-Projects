# import heapq
# from functools import total_ordering
# import heapq
# class Solution:
#     @total_ordering
#     class Wrap:
#         def __init__(self, v):
#             self.v = v

#         def __lt__(self, o):
#             return self.v > o.v  # Reverse for Max Heap

#         def __eq__(self, o):
#             return self.v == o.v
        
#     def lastStoneWeight(self, stones: list[int]) -> int:
#         wh = list(map(self.Wrap, stones))
#         heapq.heapify(wh)
#         while(len(wh) >= 2):
#             y = heapq.heappop(wh).v
#             x = heapq.heappop(wh).v
#             if(y >x ):
#                 heapq.heappush(wh, self.Wrap(y-x))
#         if(len(wh)):
#             return wh[0].v
#         else:
#             return 0

from functools import total_ordering
import heapq
import math
class Solution:
    @total_ordering
    class Wrap:
        def __init__(self, v):
            self.v = v

        def __lt__(self, o):
            return self.v > o.v  # Reverse for Max Heap

        def __eq__(self, o):
            return self.v == o.v
    def pickGifts(self, gifts: list[int], k: int) -> int:
        max_heap = (list(map(self.Wrap, gifts)))
        heapq.heapify(max_heap)
        result = [ ]
        while(k > 0):
            result.append(int(math.sqrt(heapq.heappop(max_heap).v)))
            k  = k-1
            print(result)
        result = result + [l.v for l in max_heap]
        print(result)
        return sum(result)
print(Solution().pickGifts([25,64,9,4,100],4))
        
        