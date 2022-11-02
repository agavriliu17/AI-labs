import random


class Node:
        name = ''
        links = []
        link_weights = []

        def __init__(self, name, links, link_weights):
            self.name = name
            self.links = links
            if link_weights == []:
                self.link_weights = [random.uniform(0,1)] * len(links)
            else:
                self.link_weights = link_weights
        
        def link_node(self, node):
            self.links.append(node)
        
        def update_weight(self, weight_index, new_weight):
            self.link_weights[weight_index] = new_weight
        
        def get_link_params(self, index):
            return (self.links[index], self.link_weights[index])

        def show_data(self):
            print('Name: {}\n'.format(self.name))
            for index in range(0, len(self.links)):
                print('Weight = {} to node: {}\n'.format(self.link_weights[index], self.links[index]))

