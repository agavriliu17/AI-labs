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
        self.player1['moves'] = [line1[1], line1[2]]

        line1 = f.readline().split()
        self.player2['name'] = line1[0]
        self.player2['moves'] = [line1[1], line1[2]]

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
        return max_index


if __name__ == "__main__":
    game = Game("problem.txt")
    print(game.get_dominant_strategy(1))

