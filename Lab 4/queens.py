from threading import current_thread
import numpy as np
class Board:
    size = 0 # instance size, also equals to the number of queens
    board = [] # 0 - free slot, -1 - block, -2 - queen fire

    # Constructor for 2 or 1 arguments: 
    # 1 - file name from where the data should be extracted
    # 2 - (instance size, list of coordinates for blocks)
    def __init__(self, *args):
        if len(args) == 2:
            self.size = args[0]
            blocks = args[1]
            for i in range(self.size):
                row = [0] * self.size
                self.board.append(row)
            for block in blocks:
                self.board[block[0]][block[1]] = -1
            self.np_board = np.matrix(self.board)
        elif len(args) == 1:
            board_info = self.read_instance(args[0])
            self.size = board_info[0]
            blocks = board_info[1]
            for i in range(self.size):
                row = [0] * self.size
                self.board.append(row)
            for block in blocks:
                self.board[block[0]][block[1]] = -1
            self.np_board = np.matrix(self.board)    

    # Checks if there are available slots on the given row 
    # (a slot is available if it is not blocked and isn't being hit by another queen)
    def is_row_correct(self, row):
        available_slots = False
        for col in range(self.size):
            if self.board[row][col] == 1:
                return False
            if self.board[row][col] == 0:
                available_slots = True
        return available_slots

    # Checks if there are available slots on the given column 
    # (a slot is available if it is not blocked and isn't being hit by another queen)
    def is_column_correct(self, col):
        available_slots = False
        for row in range(self.size):
            if self.board[row][col] == 1:
                return False
            if self.board[row][col] == 0:
                available_slots = True
        return available_slots

    # Checks if the queen on the coordinate [row, col] doesn't strike other queens on the left and above diagonal
    def check_left_up_diagonal(self, row, col):
        current_row = row
        current_col = col
        while current_col >= 0 and current_row >= 0:
            if self.board[current_row][current_col] == 1:
                return False
            current_col -= 1
            current_row -= 1
        return True
    
    # Checks if the queen on the coordinate [row, col] doesn't strike other queens on the left and below diagonal
    def check_left_down_diagonal(self, row, col):
        current_row = row
        current_col = col
        while current_col >= 0 and current_row < self.size:
            if self.board[current_row][current_col] == 1:
                return False
            current_col -= 1
            current_row += 1
        return True
    
    # Checks if the queen on the coordinate [row, col] doesn't strike any previously placed 
    # queen on the diagonal (only left is considered as there would be no queens to the right yet) 
    def check_left_diagonals(self, row, col):
        return self.check_left_down_diagonal(row, col) and self.check_left_up_diagonal(row, col)

    # Checks if the queen on the coordinate [row, col] doesn't strike any previously placed queen
    def is_correct(self, row, column):
        return self.is_row_correct(row) and self.is_column_correct(column) and self.check_left_diagonals(row, column)
    
    # Returns a list of rows available for placing the queen 
    # (queen parameter represents the queen's order number, or in other words - the column)
    def get_potential_rows(self, queen):
        rows = []
        for row in range(self.size):
            if self.is_correct(row, queen) and self.board[row][queen] != -1:
                rows.append(row)
        return rows

    # Displays current state of the game board
    def show(self):
        for row in self.board:
            print(row)
    
    # Places a queen on the coordinate [row, column]
    def place_queen(self, coordinate):
        if self.board[coordinate[0]][coordinate[1]] == 0:
            self.board[coordinate[0]][coordinate[1]] = 1
            #self.process_queen(coordinate)
            return True
        return False
    
    def place_queen_copy(self, coordinate, board):
        if board[coordinate[0]][coordinate[1]] == 0:
            board[coordinate[0]][coordinate[1]] = 1
            #self.process_queen(coordinate)
            return True
        return False
    
    def process_queen_copy(self, coordinate, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(i == coordinate[0] or j == coordinate[1] or i-coordinate[0] == j - coordinate[1] or i-coordinate[0] == coordinate[1] -j):
                    if(board[i][j] == 0):
                        board[i][j] = -2

    # OBSOLETE - checked where could the queen at the provided coordinate attack on the table
    def process_queen(self, coordinate):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(i == coordinate[0] or j == coordinate[1] or i-coordinate[0] == j - coordinate[1] or i-coordinate[0] == coordinate[1] -j):
                    if(self.board[i][j] == 0):
                        self.board[i][j] = -2

    def clear_queen(self, row, col, board):
        print(row)
        #self.board[row][col] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(i == row or j == col or i-row == j - col or i-row == col -j):
                    if(board[i][j] == 0):
                        board[i][j] = 0

    #Prints all the columns (domains) - not used in the algorithm
    def show_domains(self):
        domains = []
        for j in range(len(self.board[0])):
            domain = []
            for i in range(len(self.board)):
                domain.append(self.board[i][j])
            domains.append(domain)
        print(domains)
        return domains

    #Reads instance from file input
    def read_instance(self, file):
        f = open(file, 'r')
        line1 = f.readline()
        line_split = line1.split()
        size = int(line_split[len(line_split)-1])
        line2 = f.readline()
        line_split = line2.split('=  ')
        instance = line_split[1].replace('[','').replace(']]\n','').replace(']','.').replace('., ',';').replace(', ',',').split(';')

        instance_list = []
        for element in instance:
            values = str(element).split(',')
            instance_list.append([int(values[0])-1, int(values[1])-1])
        return (size, instance_list)

    #Returns all available slots on the board for a potential placement of the next queen
    def get_unassigned_from_constraint(self, queen):
        result = []
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0 and self.is_correct(row, col):
                    result.append((row, col))
        return result

    # Checks if the current domain remains viable after placing a queen on the coordinate [row, queen] 
    # (remember that queen parameter coincides with the column)
    def forward_check(self, row, queen):
        current_domain = self.get_potential_rows(queen)
        temporary_domain = list(current_domain)
        for potential_row in current_domain:
            if not self.is_correct(potential_row, queen):
                temporary_domain.remove(potential_row)

        # If it returns True, then the domain is exhausted
        return len(temporary_domain) == 0

    def solve_NQueen_FC(self, queen): 
        # queen represents the queen number or the column (ex: queen = 2 => it is the third queen to be placed
        # or in other words, the column that is being researched is the column 2,
        # as we already placed a queen per column on the previous ones)

        # if the current queen is the n-th queen, where n = size of the board, we should stop
        if queen == self.size:
            self.show()
            return True

        potentialRows = self.get_potential_rows(queen)

        for row in potentialRows:
            # trying to place a queen on every available row
            self.place_queen([row, queen])

            # considering that the domain is still available
            domain_exhausted = False 

            # looping through all still available potential future queen positions
            for element in self.get_unassigned_from_constraint(queen):
                if self.forward_check(element[0], element[1]):
                    # The domain is exhausted if we place the queen at the current coordinates: [row, queen]
                    domain_exhausted = True 
                    break
            
            # The domain is still available, so we can continue
            if not domain_exhausted:
                # Checking for the next column (queen)
                if self.solve_NQueen_FC(queen+1):
                    return True

             # Resetting the choice in case of a failure
            self.board[row][queen] = 0
    
    def get_minimum_remaining_values(self, queen, potentialRows):
        min_remaining_values = self.size
        next_row = 0

        for row in potentialRows:
            remaining_values = len(self.get_unassigned_from_constraint(queen))

            if remaining_values > min_remaining_values:
                min_remaining_values = remaining_values
                next_row = row
        
        print(next_row)
        return next_row

    def get_free_rows(self, col, board):
        rows = []
        index = 0
        for row in board:
            if row[col] == 0:
                rows.append(index)
            index += 1
        return rows

    def sort_cols(self, columns):
        scores = dict()
        for col in columns:
            score = 0
            for row in range(0, self.size):
                if self.board[row][col] == 0:
                    score += 1
            scores[col] = score
        scores = dict(sorted(scores.items(), key=lambda item: item[1]))
        return list(scores.keys())

    def get_free_cols(self, board):
        cols = []
        for col in range(self.size):
            col_is_free = True
            for row in range(self.size):
                if board[row][col] == 1:
                    col_is_free = False
            if col_is_free:
                cols.append(col)
        return cols

    def update_table(self):
        board_copy = list(self.board)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    self.place_queen_copy([i,j],board_copy)
                    self.process_queen_copy([i,j], board_copy)
        return board_copy


    def get_MRV(self):
        board_copy = self.update_table()
        cols = self.get_free_cols(board_copy)
        cols = self.sort_cols(cols)
        free_rows = self.get_free_rows(cols[0], board_copy)
        result = []
        for row in free_rows:
            result.append([cols[0], row])
        return result

    def solve_NQueen_MRV(self, queen): 
        # queen represents the queen number or the column (ex: queen = 2 => it is the third queen to be placed
        # or in other words, the column that is being researched is the column 2,
        # as we already placed a queen per column on the previous ones)

        # if the current queen is the n-th queen, where n = size of the board, we should stop
        if queen == self.size:
            self.show()
            return True

        potentialRows = self.get_potential_rows(queen)

        for row in potentialRows:
            # trying to place a queen on every available row
            self.place_queen([row, queen])

            # considering that the domain is still available
            domain_exhausted = False 

            # looping through all still available potential future queen positions
            for element in self.get_MRV():
                if self.forward_check(element[0], element[1]):
                    # The domain is exhausted if we place the queen at the current coordinates: [row, queen]
                    domain_exhausted = True 
                    break
            
            # The domain is still available, so we can continue
            if not domain_exhausted:
                # Checking for the next column (queen)
                if self.solve_NQueen_FC(queen+1):
                    return True

             # Resetting the choice in case of a failure
            self.board[row][queen] = 0


    


if __name__ == '__main__':
    #b1 = Board(4, [[1, 3], [1, 2], [2, 2]])
    # 'block-10-58-1.param'
    # 'block-10-50-11.param'
    # 'block-10-50-14.param'
    #
    #
    b1 = Board('block-10-50-11.param')
    #b1.show()
    b1.solve_NQueen_MRV(0)
