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
            line_split = line.split()

            for i in range(len(line_split)):
                parsed = line_split[i].split('/')
                self.moves.append((int(parsed[0]), int(parsed[1])))

            line = f.readline()



if __name__ == "__main__":
    game = Game("problem.txt")

