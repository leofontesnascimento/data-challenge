import argparse


N = 0
TOTAL_SOLUTIONS = 0
QUEEN_CHAR = '[Q]'
EMPTY_CHAR = '[ ]'


def show_solution(positions):
    # print a board when a solution was found
    for row in range(N):
        line = ''
        for column in range(N):
            if positions[row] == column:
                line += '{} '.format(QUEEN_CHAR)
            else:
                line += '{} '.format(EMPTY_CHAR)
        print(line)
    
    print('\n')


def verify_place(positions, ocuppied_rows, column):
    # verifying if a place is under attack by any queen
    for i in range(ocuppied_rows):
        if positions[i] == column \
            or positions[i] - i == column - ocuppied_rows \
                or positions[i] + i == column + ocuppied_rows:
                    return False

    # if no have attack is able to place it
    return True


def place_queen(positions, row):
    global TOTAL_SOLUTIONS
    # trying to place a queen on row
    # verifying if all n rows are occupied
    if row == N:
        show_solution(positions)
        TOTAL_SOLUTIONS += 1
    else:
        # for each column in row try to place a queen
        for column in range(N):
            if verify_place(positions, row, column):
                positions[row] = column
                place_queen(positions, row + 1)


def main():
    print('solving problem for {n} queens and a board {n}x{n}...'.format(n=N))
    # creating all unmarked positions
    positions = [-1] * N
    print('positions: ', positions)
    # placing first queen
    place_queen(positions, 0)
    # showing total solutions
    print('solved problem for {n} queens and a board {n}x{n}!'.format(n=N))
    print('found {} distinct solutions!'.format(TOTAL_SOLUTIONS))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='N Queens Solver')
    parser.add_argument('N', nargs='?')

    args = parser.parse_args()
    N = int(args.N)
    main()
