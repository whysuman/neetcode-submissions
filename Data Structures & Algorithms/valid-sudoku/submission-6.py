class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = defaultdict(set)
        box_set = defaultdict(set)
        for row in range(len(board)):
            row_set = set()
            for col in range(len(board[row])):
                print(f"row:{row} and col:{col} and board[row][col]:{board[row][col]}")
                if board[row][col] == ".":
                    continue
                box_row = row//3
                box_col = col//3
                box_indx = box_row*3 + box_col
                if board[row][col] in box_set[box_indx]:
                    return False
                if board[row][col] in row_set:
                    return False
                if board[row][col] in col_set[col]:
                    return False   
                row_set.add(board[row][col])
                col_set[col].add(board[row][col])
                box_set[box_indx].add(board[row][col])
                # print(col_set)
        return True
            

        