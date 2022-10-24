from threading import current_thread
import numpy as np
class Board:
    size = 0 # instance size, also equals to the number of queens
    board = [] # 0 - free slot, -1 - block, -2 - queen fire

    #constructor for 2 or 1 arguments: 
    #                   1 - file name from where the data should be extracted
    #                   2 - (instance size, list of coordinates for blocks)
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

    #Checks if there are available slots on the given row (a slot is available if it is not blocked
    #                                                      and isn't being hit by another queen)
    def is_row_correct(self, row):
        available_slots = False
        for col in range(self.size):
            if self.board[row][col] == 1:
                return False
            if self.board[row][col] == 0:
                available_slots = True
        return available_slots
    #Checks if there are available slots on the given column (a slot is available if it is not blocked
    #                                                      and isn't being hit by another queen)
    def is_column_correct(self, col):
        available_slots = False
        for row in range(self.size):
            if self.board[row][col] == 1:
                return False
            if self.board[row][col] == 0:
                available_slots = True
        return available_slots
    #Checks if the queen on the coordinate [row, col] doesn't strike other queens on the left and above diagonal
    def check_left_up_diagonal(self, row, col):
        current_row = row
        current_col = col
        while current_col >= 0 and current_row >= 0:
            if self.board[current_row][current_col] == 1:
                return False
            current_col -= 1
            current_row -= 1
        return True
    
    #Checks if the queen on the coordinate [row, col] doesn't strike other queens on the left and below diagonal
    def check_left_down_diagonal(self, row, col):
        current_row = row
        current_col = col
        while current_col >= 0 and current_row < self.size:
            if self.board[current_row][current_col] == 1:
                return False
            current_col -= 1
            current_row += 1
        return True
    
    #Checks if the queen on the coordinate [row, col] doesn't strike any previously placed queen on the diagonal
    #                                                      (only left is considered as there would be no queens to the right yet) 
    def check_left_diagonals(self, row, col):
        return self.check_left_down_diagonal(row, col) and self.check_left_up_diagonal(row, col)

    #Checks if the queen on the coordinate [row, col] doesn't strike any previously placed queen
    def is_correct(self, row, column):
        return self.is_row_correct(row) and self.is_column_correct(column) and self.check_left_diagonals(row, column)
    
    #Returns a list of rows available for placing the queen (queen parameter represents the queen's order number
    #                                                        or in other words - the column)
    def get_potential_rows(self, queen):
        rows = []
        for row in range(self.size):
            if self.is_correct(row, queen) and self.board[row][queen] != -1:
                rows.append(row)
        return rows

    #Displays current state of the game board
    def show(self):
        for row in self.board:
            print(row)
    
    #Places a queen on the coordinate [row, column]
    def place_queen(self, coordinate):
        if self.board[coordinate[0]][coordinate[1]] == 0:
            self.board[coordinate[0]][coordinate[1]] = 1
            #self.process_queen(coordinate)
            return True
        return False

    #OBSOLETE - checked where could the queen at the provided coordinate attack on the table
    def process_queen(self, coordinate):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(i == coordinate[0] or j == coordinate[1] or i-coordinate[0] == j - coordinate[1] or i-coordinate[0] == coordinate[1] -j):
                    if(self.board[i][j] == 0):
                        self.board[i][j] = -2

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

    #Checks if the current domain remains viable after placing a queen on the coordinate [row, queen] (remember that queen parameter
    #                                                                                                  coincides with the column)
    def forward_check(self, row, queen):
        current_domain = self.get_potential_rows(queen)
        temporary_domain = list(current_domain)
        for potential_row in current_domain:
            if not self.is_correct(potential_row, queen):
                temporary_domain.remove(potential_row)
        return len(temporary_domain) == 0 # If it returns True, then the domain is exhausted

    #Solve the N Queen Problem using Forward Check algorithm
    def solve_NQueen_FC(self, queen): #queen represents the queen number or the column (ex: queen = 2 => it is the third queen to be placed
                            #                                           or in other words, the column that is being researched is the column 2
                            #                                           , as we already placed a queen per column on the previous ones)
        if queen == self.size: #if the current queen is the n-th queen, where n = size of the board
            self.show() # in that case we found a solution
            return True
        potentialRows = self.get_potential_rows(queen) # Get potential rows for placing the queen
        for row in potentialRows:
            self.place_queen([row, queen]) # trying to place a queen on every available row
            domain_exhausted = False # considering that the domain is still available
            for element in self.get_unassigned_from_constraint(queen): # looping through all still available potential future queen positions
                if self.forward_check(element[0], element[1]):
                    domain_exhausted = True # The domain is exhausted if we place the queen at the current coordinates: [row, queen]
                    break
            if not domain_exhausted: # The domain is still available
                if self.solve_NQueen_FC(queen+1): # Checking for the next column (queen)
                    return True
            self.board[row][queen] = 0 # Reseting the choice in case of a failure

if __name__ == '__main__':
    #b1 = Board(4, [[1, 3], [1, 2], [2, 2]])
    b1 = Board('block-10-58-1.param')
    # b1.show()
    b1.solve_NQueen_FC(0)
