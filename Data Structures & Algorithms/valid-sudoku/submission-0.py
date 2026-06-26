class Solution:

    """
    ['.', '.', '.',   '.', '5', '.',   '.', '1', '.']
    ['.', '4', '.',   '3', '.', '.',   '.', '.', '.']
    ['.', '.', '.',   '.', '.', '3',   '.', '.', '1']

    ['8', '.', '.',   '.', '.', '.',   '.', '2', '.']
    ['.', '.', '2',   '.', '7', '.',   '.', '.', '.']
    ['.', '1', '5',   '.', '.', '.',   '.', '.', '.']
    
    ['.', '.', '.',   '.', '.', '2',   '.', '.', '.']
    ['.', '2', '.',   '9', '.', '.',   '.', '.', '.']
    ['.', '.', '4',   '.', '.', '.',   '.', '.', '.']
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                num = board[row][col]
                if num == ".":
                    continue
                
                grid_idx = (row//3)*3 + (col//3)
                if num in rows[row]:
                    return False
                elif num in cols[col]:
                    return False
                elif num in grids[grid_idx]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                grids[grid_idx].add(num)

        return True