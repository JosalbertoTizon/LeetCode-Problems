class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in columns[j]:
                    return False
                columns[j].add(board[i][j])
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in squares[(i // 3) * 3 + j // 3]:
                    return False
                squares[(i // 3) * 3 + j // 3].add(board[i][j])
        return True
