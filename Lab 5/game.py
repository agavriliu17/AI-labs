class Game:
    player1 = {}
    player2 = {}
    moves = []

    def __init__(self, path):
        self.read_instance(path)

        print(self.player1)
        print(self.player2)
        print(self.moves)


    def read_instance(self, path):
        f = open(path, 'r')
        line1 = f.readline().split()
        self.player1['name'] = line1[0]
        self.player1['moves'] = line1[1:]

        line1 = f.readline().split()
        self.player2['name'] = line1[0]
        self.player2['moves'] = line1[1:]

        line = f.readline()

        while line != '':
            moves_line = []
            line_split = line.split()

            for i in range(len(line_split)):
                parsed = line_split[i].split('/')
                moves_line.append((int(parsed[0]), int(parsed[1])))
            self.moves.append(moves_line)
            line = f.readline()
    
    def get_dominant_strategy(self, player):
        if player not in (1,2):
            raise ValueError('Invalid player number!')
        player -= 1 #getting the right index for the player
        strategy_points = []
        #Different methods to calculate points for each player
        if not player: #Player 1
            for line in range(0, len(self.moves)):
                point_sum = 0
                for column in range(0, len(self.moves[0])):
                    point_sum += self.moves[line][column][player]
                strategy_points.append(point_sum/len(self.moves[0]))
        else: #Player 2
            for column in range(0, len(self.moves[0])):
                point_sum = 0
                for line in range(0, len(self.moves)):
                    point_sum += self.moves[line][column][player]
                strategy_points.append(point_sum/len(self.moves))
        
        max_index = 0
        max_point = 0
        index = 0
        for p in strategy_points:
            if p > max_point:
                max_point = p
                max_index = index
            index += 1

        if(player == 0):
            strategy = self.player1['moves'][max_index]
        else:
            strategy = self.player2['moves'][max_index]

        print('Player ' + str(player + 1) + ' has a dominant strategy: ' + strategy)
        return max_index

    def get_nash_equilibrium(self, player):
        if player not in (1,2):
            raise ValueError('Invalid player number!')
        best_strategies_matrix = []
        if player == 1:
            for column in range(0, len(self.moves[0])):
                best_move = 0
                best_score = 0
                for line in range(0, len(self.moves)):
                    score = self.moves[line][column][0] - self.moves[line][column][1]
                    if score > best_score:
                        best_score = score
                        best_move = line
                best_strategies_matrix.append((best_move, column))
        else:
            for line in range(0, len(self.moves)):
                best_move = 0
                best_score = 0
                for column in range(0, len(self.moves[0])):
                    score = self.moves[line][column][1] - self.moves[line][column][0]
                    if score > best_score:
                        best_score = score
                        best_move = column
                best_strategies_matrix.append((line, best_move))
        return best_strategies_matrix
        

if __name__ == "__main__":
    game = Game("problem.txt")
    print('---------------------------------------')
    game.get_dominant_strategy(1)
    print(game.get_nash_equilibrium(2))

