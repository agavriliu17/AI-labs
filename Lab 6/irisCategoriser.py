import random
from neuronNode import Node

class Neural_Network:
    # data structure: [sepal length, sepal width, petal length, petal width, class]
    #                   number,         number,     number,      number,      0|1|2 
    train_data = []
    test_data = []
    input_nodes = []
    output_nodes = []
    hidden_nodes = []
    input_size = 0
    output_size = 0
    hidden_size = 0
    learning_rate = 0.2
    max_epochs = 5
    
    def __init__(self, data_path):
        f = open(data_path, 'r')
        line = f.readline()
        all_data = []
        while line != '':
            all_data.append(line.replace('\n','').split(','))
            line = f.readline()
        random.shuffle(all_data)
        mid = len(all_data)//2
        self.test_data = all_data[0:mid]
        self.train_data = all_data[mid:]
        self.output_nodes = [Node('Setosa', [], []), Node('Versicolour', [], []), Node('Virginica', [], [])]
        self.hidden_nodes = [Node('h1', self.output_nodes, []),
                             Node('h2', self.output_nodes, []), 
                             Node('h3', self.output_nodes, []),
                             Node('h4', self.output_nodes, [])]
        self.input_nodes = [Node('sl', self.hidden_nodes, []),
                            Node('sw', self.hidden_nodes, []), 
                            Node('pl', self.hidden_nodes, []), 
                            Node('pw', self.hidden_nodes, [])]
        
        self.input_size = len(self.input_nodes)
        self.output_size = len(self.output_nodes)
        self.hidden_size = len(self.hidden_nodes)

    def show_all_data(self):
        print('Test data:\n{}'.format(self.test_data))
        print('\nTrain data:\n{}'.format(self.train_data))

    def show_parameters(self):
        print('Learning Rate = {}\nMaximum number of epochs = {}\n---\nInput nodes (size = {}):\n{}\n---\nHidden nodes (size = {}):\n{}\n---\nOutput nodes (size = {}):\n{}\n'.format(self.learning_rate, self.max_epochs, self.input_size, self.input_nodes, self.hidden_size, self.hidden_nodes, self.output_size, self.output_nodes))

    def set_parameters(self, learning_rate, max_epochs):
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs

    def show_input_nodes(self):
        for node in self.input_nodes:
            node.show_data()
    
    def show_hidden_nodes(self):
        for node in self.hidden_nodes:
            node.show_data()
    
    def show_output_nodes(self):
        for node in self.output_nodes:
            node.show_data()

if __name__ == '__main__':
    rn = Neural_Network('iris.data')
    rn.show_all_data()
    print('\n---\n')
    rn.show_parameters()
    print('\n---\n')
    rn.show_input_nodes()
    print('\n---\n')
    rn.show_hidden_nodes()
    print('\n---\n')
    rn.show_output_nodes()