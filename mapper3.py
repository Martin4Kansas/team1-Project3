#!/usr/bin/env python

import csv
import sys
import json

SEP = "\t"

class Mapper(object):

    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep    = sep
        with open('v.json') as f:
            self.v = json.load(f)

    def emit(self, key, value):
        sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

    def map(self):
        first_row = True
        n = 1
        beta = 0.85
        reader = csv.reader(self.stream)
        for row in reader:
            if first_row:
                n = float(row[0])
                self.emit('n', str(n))
                first_row = False
            else:
                from_node = row[0]
                to_node   = row[1]
                to_prob   = float(row[2])
                v_prob    = float(self.v[from_node])
                prob      = v_prob * to_prob * beta
                self.emit(to_node, str(prob))

if __name__ == '__main__':
    mapper = Mapper(sys.stdin)
    mapper.map()
