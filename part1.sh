#!/bin/bash
cat M.csv | python initializer3.py
cat M.csv | python mapper3.py | python reducer3.py
cat M.csv | python mapper3.py | python reducer3.py