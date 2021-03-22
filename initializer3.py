#!/usr/bin/env python

import csv
import sys
import json

class Initializer(object):
    def __init__(self, stream):
        self.stream = stream
        # self.nodes = {}
        self.num_connections = {}
        self.destinations = {}

    def emit(self, value):
        sys.stdout.write("%s\n" % (value))

    def initialize(self, commas=False):
        if commas == True:
            delim = ','
        else:
            delim = '\t'
        reader = csv.reader(self.stream, delimiter = delim)
        in_node_counter = {}
        has_third_column = False
        for row in reader:
            if len(row) == 1:
                commas = True
                self.initialize(True)
                return
            elif len(row) > 2:
                has_third_column = True
            src_node = row[0]
            dest_node = row[1]
            if not has_third_column:
                if src_node not in self.destinations.keys():
                    self.destinations[src_node] = [dest_node]
                else:
                    self.destinations[src_node].append(dest_node)
            else:
                if src_node not in self.destinations.keys():
                    self.destinations[src_node] = [row[1]]
                else:
                    self.destinations[src_node].append(row[1])
        self.num_connections = {key: len(value) for key, value in self.destinations.items()}
        with open('M.csv', "w") as outfile:
            outfile.write(str(len(self.destinations)) + '\n')
            for source, destinations in self.destinations.items():
                prob = 1.0 / self.num_connections[source]
                for destination in destinations:
                    outfile.write(str(source) + ',' + str(destination) + ',' + str(prob) + '\n')
        # output = ','.join(str(val) for val in [initial_prob] * len(self.node_list))
        # with open('v.csv', "w") as outfile:
        #     outfile.write(output)
        initial_prob = 1.0/len(self.destinations)
        output = {source: initial_prob for source in self.destinations.keys()}
        with open('v.json', 'w') as f:
            json.dump(output, f)
        if len(str(output)) > 100:
            self.emit(str(output)[:100])
        else:
            self.emit(str(output))

if __name__ == '__main__':
    initializer = Initializer(sys.stdin)
    initializer.initialize()
