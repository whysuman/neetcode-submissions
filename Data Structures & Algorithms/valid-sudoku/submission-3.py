class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_track = [set() for _ in range(9)]
        row_track = [set() for _ in range(9)]

        square_track = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                curr = board[row][col]

                if curr == ".":
                    continue

                if curr in col_track[col]:
                    return False
                else:
                    col_track[col].add(curr)

                if curr in row_track[row]:
                    return False
                else:
                    row_track[row].add(curr)

                sindx = int(row/3)*3 + int(col/3)
                print(sindx,row,col)

                if curr in square_track[sindx]:
                    return False
                else:
                    square_track[sindx].add(curr)

        return True

       