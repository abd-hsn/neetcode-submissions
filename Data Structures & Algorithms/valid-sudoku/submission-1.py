class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            counter = [ 0]*9

            row = board[i]
            for ri in row:
                if ri ==".":
                    continue
                counter[int(ri)-1]-=1

            if min(counter) < -1:
                return False
            
        for i in range(9):
            counter = [ 0]*9
            for row in board:
                val = row[i]
                if val ==".":
                    continue
                counter[int(val)-1]-=1
            if min(counter) < -1:
                return False
        
        # For top left cube
        for cube in [0,3,6]:
            counter = [ 0]*9
            for r in range(9):
                for c in range(3):
                    val = board[r][c+cube]
                    if val == '.':
                        continue
                    counter[int(val)-1]-=1
                if min(counter) < -1:
                    return False

                if r == 2 or r == 5:
                    counter = [ 0]*9
                
                
        return True
        
