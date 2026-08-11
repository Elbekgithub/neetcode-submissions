from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = [str(i) for i in range(1, 10)]
        l = len(board)
        columns = defaultdict(list)
        boxes = defaultdict(list)
        for i in range(l):
            row_list = []
            for j in range(l):
                cell = board[i][j]
                
                if cell == ".":
                    continue
                if cell not in digits:
                    return False
                if cell in row_list:
                    return False
                else:
                    row_list.append(cell)
                if cell in columns[j]:
                    return False
                else:
                    columns[j].append(cell)
                
                box_key = (i // 3, j // 3)
                if cell in boxes[box_key]:
                    return False
                else:
                    boxes[box_key].append(cell)
        return True
                
