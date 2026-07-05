class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        column={}
        square={}
        for i in range(len(board)):
            for j in range(len(board)):
                if i not in row:
                    row[i]=set()
                if j not in column:
                    column[j]=set()
                if (i//3,j//3) not in square:
                    square[i//3,j//3]=set()
                if board[i][j]==".":
                    continue
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])
                if board[i][j] in column[j]:
                    return False
                column[j].add(board[i][j])
                if board[i][j] in square[i//3,j//3]:
                    return False
                square[i//3,j//3].add(board[i][j])
        return True
                
                    

    
        