# Name: Xi (Benson) Chen, Zhiyu (Yuki) Pu
# Student ID: Chen: 3617 1540, Pu: 2783 7481
# Email: chexfeii@umich.edu, zhiyupu@umich.edu
# How we used generative AI:

import os
import csv

#Read penguins.csv file
def load_data(f):

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    data = []

    with open(f, 'r') as file:
        r = csv.DictReader(file)

        for row in r:
            data.append(row)

    return data

#Drops rows with invalid or missing data
def clean_and_cast(data):

    cleaned_data = []

    for row in data:
        
        new_row = {}

        for key, value in row.items():
            cleaned_value = str(value).strip()

            if cleaned_value == '' or cleaned_value.lower() == 'na':
                new_row[key] = None

            else:
                try:
                    new_row[key] = float(cleaned_value)

                except ValueError:
                    new_row[key] = cleaned_value

        cleaned_data.append(new_row)

    return cleaned_data

if __name__ == '__main__':
    
    data = load_data('penguins.csv')
    cleaned_data = clean_and_cast(data)

    print(cleaned_data)