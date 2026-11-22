def sudokuSolve(matrix):
    board = [list(row) for row in matrix]
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []

    for r in range(9):
        for c in range(9):
            ch = board[r][c]
            if ch == "0":
                empties.append((r, c))
            else:
                b = (r // 3) * 3 + (c // 3)
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def backtrack(idx):
        if idx == len(empties):
            return True

        r, c = empties[idx]
        b = (r // 3) * 3 + (c // 3)

        for d in digits:
            if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                if backtrack(idx + 1):
                    return True

                board[r][c] = "0"
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

        return False

    backtrack(0)
    return ["".join(row) for row in board]