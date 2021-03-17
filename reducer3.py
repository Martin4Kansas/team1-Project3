#!/usr/bin/env python

import sys

from itertools import groupby
from operator import itemgetter

SEP = "\t"

class Reducer(object):

    def __init__(self, stream, sep=SEP):
        self.stream   = stream
        self.sep      = sep
        self.val_dict = {}
        self.new_vals = []

    def emit(self, key, value):
        sys.stdout.write("%s%s%s\n" % (key, self.sep, value))

    def reduce(self):
        for current, group in groupby(self, itemgetter(0)):
            if current not in self.val_dict.keys():
                self.val_dict[str(current)] = 0
            for item in group:
                self.val_dict[current] += item[1]
        for key in sorted(self.val_dict.keys()):
            self.emit(key, self.val_dict[key])
            self.new_vals.append(self.val_dict[key])
        output = ','.join(str(val) for val in self.new_vals)
        with open('v.csv', "w") as outfile:  
            outfile.write(output)

    def __iter__(self):
        for line in self.stream:
            try:
                parts = line.split(self.sep)
                yield parts[0], float(parts[1])
            except:
                continue

if __name__ == '__main__':
    reducer = Reducer(sys.stdin)
    reducer.reduce()

