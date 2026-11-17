
class Solution(object):
    def solveSudoku(self, board):

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)

        def backtrack(pos):
            if pos == len(empty):
                return True

            i, j = empty[pos]
            b = (i//3)*3 + j//3

            for num in "123456789":
                if num not in rows[i] and num not in cols[j] and num not in boxes[b]:

                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[b].add(num)

                    if backtrack(pos + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[b].remove(num)

            return False

        backtrack(0)
