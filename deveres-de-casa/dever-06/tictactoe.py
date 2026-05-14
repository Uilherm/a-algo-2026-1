"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    num_x = 0
    num_o = 0
    for row in board:
        num_x += row.count(X)
        num_o += row.count(O)

    if num_x == num_o:
        return X
    else:
        return O
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError


def actions(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                moves.append((i, j))
    
    return moves
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    i, j = action
    
    if board[i][j] is not None:
        raise Exception
    
    result_board = copy.deepcopy(board)
    result_board[i][j] = player(board)
    
    return result_board
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    first_col = second_col = third_col = diag = anti_diag = ""

    for i in range(3):
        if board[i].count(X) == 3:
            return X
        if board[i].count(O) == 3:
            return O

        if board[i][0]:
            first_col += board[i][0]
        if board[i][1]:
            second_col += board[i][1]
        if board[i][2]:
            third_col += board[i][2]

        if board[i][i]:
            diag += board[i][i]
        if board[i][2-i]:
            anti_diag += board[i][2-i]
    
    for cond in [first_col,second_col,third_col,diag,anti_diag]:
        if cond.count(X) == 3:
            return X
        if cond.count(O) == 3:
            return O
        
    return None
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    if winner(board):
        return True

    for row in board:
        if EMPTY in row:
            return False
    
    return True
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    victory = winner(board)
    if victory == X:
        return 1
    if victory == O:
        return -1
    return 0
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    current_player = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state)

        v = float("-inf")

        for action in actions(state):
            v = max(v, min_value(result(state, action)))

        return v

    def min_value(state):
        if terminal(state):
            return utility(state)

        v = float("inf")

        for action in actions(state):
            v = min(v, max_value(result(state, action)))

        return v

    best_action = None

    if current_player == "X":
        best_score = float("-inf")

        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

    else:
        best_score = float("inf")

        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

    return best_action
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError