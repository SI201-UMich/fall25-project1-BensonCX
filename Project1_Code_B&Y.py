# Name: Xi (Benson) Chen, Zhiyu (Yuki) Pu
# Student ID: Chen: 3617 1540, Pu: 2783 7481
# Email: chexfeii@umich.edu, zhiyupu@umich.edu
# How we used generative AI:

import os
import csv

#Read penguins.csv file
def load_data (f):

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    rows = []

    with open(f, 'r') as file:
        r = csv.DictReader(file)

        for row in r:
            rows.append(row)

    return rows

if __name__ == "__main__":
    data = load_data('penguins.csv')
    
    print(data)