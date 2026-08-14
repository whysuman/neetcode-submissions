class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_list = [set() for _ in range(9)]
        cols_list = [set() for _ in range(9)]
        boxes_list = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cell_value = board[row][col]
                curr_rowset = rows_list[row]
                curr_colset = cols_list[col]
                
                if cell_value == ".":
                    continue

                if cell_value in curr_rowset or cell_value in curr_colset:
                    return False
                
                """
                Step 1. Mapping the current cell to the cell in the current 3x3 box
                Dividing the row index r by 3 tells you which boxrow the cell is in (0, 1, or 2).
                Dividing the column index c by 3 tells you which box column the cell is in (0, 1, or 2)
                
                Step 2. Mapping the current cell to one of the 9 3x3 boxes
                Box row 0, col 0 → box 0
                Box row 0, col 1 → box 1
                Box row 0, col 2 → box 2
                Box row 1, col 0 → box 3
                Box row 1, col 1 → box 4
                Box row 1, col 2 → box 5
                Box row 2, col 0 → box 6
                Box row 2, col 1 → box 7
                Box row 2, col 2 → box 8
                """

                box_id = 3*(row//3) + col//3
                curr_box = boxes_list[box_id]
                if cell_value in curr_box:
                    return False

                cols_list[col].add(cell_value)
                rows_list[row].add(cell_value)
                boxes_list[box_id].add(cell_value)
        
        return True
                