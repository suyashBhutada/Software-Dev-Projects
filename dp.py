class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        indexes_with_zeros = set()
        for i in range(len(arr)):
            if arr[i] ==0:
                indexes_with_zeros.add(i)
        maxi = min(start + arr[start], len(arr) -1)
        mini = max(0,start-arr[start])
        visited = set()
        visited.add(start)
        q = set()
        q.add(mini)
        q.add(maxi)
        while q:
            poppes = q.pop()
            visited.add(poppes)
            if(poppes in indexes_with_zeros):
                return True
            if( min(poppes + arr[poppes], len(arr) -1) not in visited):
                q.add(min(poppes + arr[poppes], len(arr) -1))
            if(max(0,poppes-arr[poppes])  not in visited):
                q.add(max(0,poppes-arr[poppes]))
        return False

# print(Solution().canReach([5,11,18,16,21,3,19,0,16,4,9,20,2,13,0,2,23,8,19,22,16,19,19,25,25,15,7],18))


class Solution1:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if(len(s) and s[-1] == "1"):
            return False
        maxReach = min(len(s)-1, 0 + maxJump)
        minReach = min(len(s)-1, 0 + minJump)
        excluded = set()
        for i in range(1,len(s)):
            if( i<= maxReach and i >= minReach and s[i]=="0" and i not in excluded):
                if(i + minJump <= min(len(s)-1, i + maxJump)):
                    nmin = i + minJump
                    nmax = min(len(s)-1, i + maxJump)
                    if nmin > maxReach:
                        excluded = excluded | set(range(maxReach + 1,nmin))
                    maxReach = max(maxReach, nmax)
                    minReach= min(minReach,nmin)
                if(maxReach == len(s)-1):
                    return True
        return False
# print(Solution1().canReach("011100110101011011011110",4,5))


class nextP():
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if(nums[i] > nums[i-1]):
                # nums = nums[0:i-1]  + [nums[i]] + sorted([nums[i-1]] + nums[i+1:])
                nums[i-1], nums[i] = nums[i], nums[i-1]
                nums[i + 1:] = reversed(nums[i + 1:])
                original  = i
                while(i<len(nums)-1 and nums[i] > nums[i+1]):
                    nums[i+1], nums[i] = nums[i], nums[i+1]
                    i += 1
                return
        nums[:] = reversed(nums[:])
        # print(nums)
        return



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class tree:
    def sortedListToBST(self, head) -> Optional[TreeNode]:
        
        def createTree(inp,l,r):
            # if(l>=r):
            #     return None
            mid = l + (r-l)//2
            node = TreeNode(inp[mid])
            if(l <mid-1):
                ln = createTree(inp,l,mid-1)
                node.left = ln
            if(r > mid+1):
                rn = createTree(inp,mid+1,r)
                node.right = rn
            return node
        
        # temp = ListNode(-1e6,head)
        # n = 0
        # l = []
        # while head:
        #     l.append(head.val)
        #     head = head.next
        #     n +=1
        return createTree(head,0,len(head)-1)


        

# tree().sortedListToBST([-10,-3,0,5,9])

class graph:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        partA = set()
        partB = set()
        firstnonzeroind = 0
        while firstnonzeroind < len(graph)-1 and len(graph[firstnonzeroind]) == 0:
            firstnonzeroind += 1
        partA.add(firstnonzeroind)
        fill = 1

        visited = set()
        visited.add(firstnonzeroind)
        q = set(graph[firstnonzeroind])
        while q or (len(visited) < len(graph)):
            if(not q):
                firstnonzeroind = 0
                while firstnonzeroind in visited or len(graph[firstnonzeroind]) == 0:
                    firstnonzeroind += 1
                partA.add(firstnonzeroind)
                fill = 1
                visited.add(firstnonzeroind)
                q = set(graph[firstnonzeroind])

            temp = q.copy()
            q.clear()
            if(fill):
                tofill = partB
                fill = 0
            else:
                tofill = partA
                fill = 1

            for c in temp:
                if c not in visited:
                    visited.add(c)
                    tofill.add(c)
                    if len(set(graph[c]) & tofill):
                        return False
                    q = q | set(graph[c])
        return True
            

print(graph().isBipartite([[4],[],[4],[4],[0,2,3]]))

        