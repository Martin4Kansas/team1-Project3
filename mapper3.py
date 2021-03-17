#!/usr/bin/env python

import csv
import sys

SEP = "\t"

class Mapper(object):

    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep    = sep
        with open('v.csv', newline='') as f:
            self.v = list(map(float,next(csv.reader(f))))
    
    def emit(self, key, value):
        sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

    def map(self):
        reader = csv.reader(self.stream)
        for row in reader:
            from_node = int(row[0])
            to_node   = int(row[1])
            to_prob   = float(row[2])
            v_prob    = float(self.v[(from_node) - 1])
            prob      = v_prob * to_prob
#             self.emit(row[0], row[1] + SEP + str(to_prob) + SEP + str(v_prob) + SEP + str(prob) )
            self.emit(row[1], str(prob))

if __name__ == '__main__':      
    mapper = Mapper(sys.stdin)
    mapper.map()
  