import random

CELLS = 3 * 3


# ------------ Example strategy 1 ------------
def example_strategy(user_moves):
    bot_moves = []
    filled_cells = [False] * CELLS

    for user_move in user_moves:
        for cell in range(CELLS):
            if not filled_cells[cell]:
                filled_cells[cell] = True
                bot_moves.append(cell)
                break

        filled_cells[user_move] = True

    return bot_moves


def answer_example_strategy():
    # Return your answer here e.g. [1, 4, 7].
    return []


# ---------------- Strategy 1 ----------------
def strategy_1(user_moves):
    bot_moves = []
    sequence = [0, 6, 3, 2, 1, 8, 5, 7, 4]
    filled_cells = [False] * CELLS

    for user_move in user_moves:
        for cell in sequence:
            if not filled_cells[cell]:
                filled_cells[cell] = True
                bot_moves.append(cell)
                break

        filled_cells[user_move] = True

    return bot_moves


def answer_strategy_1():
    # Return your answer here.
    return [1,4,7]


# ---------------- Strategy 2 ----------------
def strategy_2(user_moves):
    bot_moves = [4]
    filled_cells = [False] * CELLS
    filled_cells[4] = True


    for user_move in user_moves[:-1]:
        filled_cells[user_move] = True
        winning_moves = get_winning_moves(filled_cells, 4)
        if winning_moves:
            bot_moves.append(winning_moves[0])
            continue
        for delta in range(1, CELLS):
            cell = (user_move + delta) % CELLS
            if not filled_cells[cell]:
                filled_cells[cell] = True
                bot_moves.append(cell)
                break

    return bot_moves

def get_winning_moves(filled_cells, cell=None):
    for i in range(CELLS):
        if filled_cells[i] and filled_cells[(i + 1) % CELLS] and filled_cells[(i + 2) % CELLS]:
            return [i, (i + 1) % CELLS, (i + 1) * CELLS, (i + 2) *CELLS]
        
        if i % 2 == 0:
            if filled_cells[i] and filled_cells[i + CELLS + 1] and filled_cells[i + 2 * CELLS + 2]:
                return [i, i + CELLS + 1, i + 2 * CELLS + 2]
        else:
            if filled_cells[i] and filled_cells[i + CELLS - 1] and filled_cells[i +2 * CELLS -2]:
                return [i, i + CELLS + 1, i + 2 * CELLS - 2]
    if cell is not None:
        for row in range(3):
            for col in range(3):
                if not filled_cells[row * CELLS + col]:
                    f_cells = []
                    if (row * CELLS + col) != cell:
                        if not filled_cells[(row + 1)%3*CELLS+col] and not filled_cells[(row -1)% 3*CELLS+col]:
                            f_cells.append((row + 1)%3*CELLS + col)
                            f_cells.append((row - 1)%3*CELLS + col)
                        if not filled_cells[row * CELLS + (col+1)%3] and not filled_cells[row*CELLS + (col - 1)% 3]:
                            f_cells.append(row * CELLS + (col + 1)% 3)
                            f_cells.append(row * CELLS + (col - 1)% 3)
    return []



def answer_strategy_2():
    # Return your answer here.
    return [4,5,8]


# ---------------- Strategy 3 ----------------
def strategy_3(user_moves):
    bot_moves = [4]
    filled_cells = [False] * CELLS
    filled_cells[4] = True
    sequence = [2, 5, 7, 8, 1, 0, 6, 4, 3]

    for user_move in user_moves[:-1]:
        filled_cells[user_move] = True
        idx = sequence.index(user_move)

        for delta in range(1, CELLS):
            cell = sequence[(idx + delta) % CELLS]
            if not filled_cells[cell]:
                filled_cells[cell] = True
                bot_moves.append(cell)
                break

    return bot_moves


def answer_strategy_3():
    # Return your answer here.
    return [4,2,0]


# ---------------- Strategy 4 ----------------
def strategy_4(user_moves):
    # Functions responsible for generating random numbers may have different
    # implementations depending on the compiler, language version and used machine.
    # We strongly recommend using our platform to test and validate their behaviour.
    random.seed(255)
    bot_moves = []
    empty_cells = list(range(CELLS))

    for user_move in user_moves:
        cell = random.choice(empty_cells)
        bot_moves.append(cell)
        empty_cells.remove(cell)
        empty_cells.remove(user_move)

    return bot_moves


def answer_strategy_4():
    # Return your answer here.
    return [2,4,1]
