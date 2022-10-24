import numpy as np
class Board:
    size = 0
    board = []
    np_board = None

    def convert_value(string_form):
        values = string_form.split(',')
        result = []
        result.append(int(values[0]))
        result.append(int(values[1]))
        return result

    def __init__(self, size, blocks):
        self.size = size
        for i in range(size):
            row = [0] * size
            self.board.append(row)
        for block in blocks:
            self.board[block[0]][block[1]] = -1
        self.np_board = np.matrix(self.board)

    def __init__(self, file):
        board_info = self.read_instance(file)
        self.size = board_info[0]
        blocks = board_info[1]
        for i in range(self.size):
            row = [0] * self.size
            self.board.append(row)
        for block in blocks:
            self.board[block[0]][block[1]] = -1
        self.np_board = np.matrix(self.board)

        
    
    def show(self):
        for row in self.board:
            print(row)
    
    def place_queen(self, coordinate):
        if self.board[coordinate[0]][coordinate[1]] == 0:
            self.board[coordinate[0]][coordinate[1]] = 1
            self.process_queen(coordinate)
            self.np_board = np.matrix(self.board)
            return True
        return False

    def process_queen(self, coordinate):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if(i == coordinate[0] or j == coordinate[1] or i-coordinate[0] == j - coordinate[1] or i-coordinate[0] == coordinate[1] -j):
                    if(self.board[i][j] == 0):
                        self.board[i][j] = -2

    def show_domains(self):
        domains = []
        for j in range(len(self.board[0])):
            domain = []
            for i in range(len(self.board)):
                domain.append(self.board[i][j])
            domains.append(domain)
        return domains

            


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
        
# b1 = Board(4, [[1, 3], [1, 2], [2, 2]])
b1 = Board('block-10-58-1.param')
b1.show()

