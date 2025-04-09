# import pandas as pd
# d = dict()
# d.update({'a': 1})
# d.update({'b': 2})
# d.update({'c': 3})  
# d.update({'a': 4})
# print(d)
# # df = pd.DataFrame(d, index=[0]) 
# # print(df)

class Solution:
    def __init__(self):
        self.ans = []
    def checkSAfe(self,board, r,c,n):
        for i in range(r,-1,-1):
            if(board[i][c] == "Q"):
                return False
        j = c
        for i in range(r,-1,-1):
            if(j <0):
                break
            if(board[i][j] == "Q"):
                return False
            j -= 1
        
        j = c
        for i in range(r,-1,-1):
            if(j == n):
                break
            if(board[i][j] == "Q"):
                return False
            j += 1
        return True
    def solve(self, board, r,n):
        if(r == n):
            self.ans.append(board.copy())
            print(self.ans)
            return
        for c in range(0,n):
            if(self.checkSAfe(board,r,c,n)):
                board[r] = board[r][:c] + 'Q' + board[r][c+1:]
                self.solve(board,r+1,n)
                board[r] = board[r][:c] + '.' + board[r][c+1:]
    def solveNQueens(self, n: int) -> list[list[str]]:
        if(n ==0):
            return [[]]
        board = ['.'* n  for i in range(n)]
        self.solve(board,0,n)
        return self.ans

print(Solution().solveNQueens(4))

        