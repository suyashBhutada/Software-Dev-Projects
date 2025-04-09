# # Definition for a binary tree node.
from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findPath(self, root: Optional[TreeNode], x: int):
#         if( root == None):
#             return None
#         if root.val ==x:
#             return [x]
#         else:
#             fl = self.findPath(root.left, x)
#             fr = self.findPath(root.right, x)
#             if fl is not None:
#                 return( [root.val] + fl )
#             if fr is not None:
#                 return( [root.val] + fr )
#             return None
#     def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
#         pathx = self.findPath(root,x)
#         pathy = self.findPath(root,y)
#         if(len(pathx) == len(pathy) & len(pathx)>2):
#             if(pathx[-2] != pathy[-2]):
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     def inOrder(self,root,ans):
#         if root == None:
#             return ans
#         else:
#             ans = self.inOrder(root.left,ans)
#             ans.append(root.val)
#             ans = self.inOrder(root.right,ans)
#             return ans


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def isValidBST(self, rooot: Optional[TreeNode]) -> bool:

        def check_left(root):
            if not root:
                return [True, "na"]
            rv = root.val
            l = check_left(root.left)
            if l[1] != "na":
                if(rv <= l.val):
                    return [False,-1]
                else:
                    return([ l[0]and rv > l[1] , rv])
            else:
                return ([True,rv])
            
        def check_right(root):
            if not root:
                return [True, "na"]
            rv = root.val
            right_root = check_right(root.right)
            if right_root[1] != "na":
                if(rv > right_root.val):
                    return [False,-1]
                else:
                    return(
                        [ right_root[0]and rv < right_root[1] 
                         , rv])
            else:
                return ([True,rv])

        def ch_int(root):
            if not root:
                return True
            llc = check_left(root.left)
            lrc = check_right(root.right)
            rrc = check_right(root.right)
            rlc = check_left(root.right)

        return ch_int(rooot)[0]
    def levelorder(self, root: Optional[TreeNode] ):
        if not root:
            return None
        else:
            q =[]
            q.append(root)
            while(q):
                print("--------------------------")
                curl = len(q)
                print(curl)
                for _ in range(curl):
                    r = (q.pop(0))
                    print(r.val, "|root")
                    if r.left:
                        print(r.left.val)
                        q.append(r.left)
                    if r.right:
                        print(r.right.val)

                        q.append(r.right)
        return
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def isLeafNode(root):
            if not root:
                return False
            if root.left is None and root.right is None:
                return True
        if(root is None):
            return False
        if(targetSum > 0):
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        if targetSum == 0:
            if isLeafNode(root):
                return True
            else:   
                return False


root = TreeNode(32)
root.left = TreeNode(26)
root.right = TreeNode(47)
root.right.right = TreeNode(56)
root.left.left = TreeNode(19)
root.left.left.right = TreeNode(27)

# print(Solution1().levelorder(root))




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution4:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        included = set()
        @cache
        def recfun(r,t,includeroot):
            if(r == None):
                return 0
            else:
                if(r.val == t):
                    ans = 1
                else:
                    ans = 0
                if includeroot:
                    a =  (ans + recfun(r.left,t-r.val,True) + recfun(r.right,t-r.val,True) )
                    if( r not in included):
                        included.add(r)
                        b = recfun(r,targetSum,False)
                    else:b = 0
                    return a + b
                else:
                    a = recfun(r.left,t-r.val,True)
                    b = recfun(r.right,t-r.val,True)
                    return a + b + ans
        return recfun(root,targetSum,False)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)

a= TreeNode(1)
a.right = TreeNode(2)
a.right.right = TreeNode(3)
a.right.right.right = TreeNode(4)
a.right.right.right.right = TreeNode(5)

c = TreeNode(-8)
c.left  = TreeNode(6)
c.right = TreeNode(8)
c.right.left =TreeNode(8)
c.right.right = TreeNode(2)
c.right.right.right = TreeNode(-2)



print(Solution4().pathSum(c,-2))

        
        