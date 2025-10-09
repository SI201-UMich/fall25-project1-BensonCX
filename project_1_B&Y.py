# Name: Xi (Benson) Chen
# Student ID: 3617 1540
# Email: chexfeii@umich.edu
# Who did I work with: Zhiyu (Yuki) Pu
# How I used generative AI:

import unittest
import os
import csv

def load_data(f):

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    rows = []

    with open(f, 'r') as file:
        r = csv.DictReader(file)
        for row in r:
            rows.append(row)


    return rows

if __name__ == '__main__':
    data = load_data('penguins.csv')
    print(data)