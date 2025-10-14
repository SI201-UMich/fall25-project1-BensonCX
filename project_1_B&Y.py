# Name: Xi (Benson) Chen, ZHiyu (Yuki) Pu
# Student ID: 3617 1540
# Email: chexfeii@umich.edu, zhiyupu@umich.edu
# How we used generative AI:

import unittest
import os
import csv
import statistics

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





    # Read the CSV
def load_data(filename):

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, filename)

    rows = []
    with open(full_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "Unnamed: 0" in row:
                del row["Unnamed: 0"]
            rows.append(row)
    return rows

def to_float(x):
    s = str(x).strip()
    if s == "" or s.lower() in ("na", "nan", "null"):
        return None 
    try:
        return float(s)
    except ValueError:
        return None
    
# Make sure to handle missing or invalid data


# Calculates average bill length/depth for males and females

def avg_bill_by_species_sex(rows):
    data = {}
    for r in rows:
        species = r.get("species", "")
        sex = r.get("sex", "")
        key = (species, sex)

        length = to_float(r.get("bill_length_mm", ""))
        depth  = to_float(r.get("bill_depth_mm", ""))
        if length is None or depth is None:
            continue

        if key not in data:
            data[key] = {"lengths": [], "depths": []}
        data[key]["lengths"].append(length)
        data[key]["depths"].append(depth)

    result = []
    for species, sex in data:
        avg_length = sum(data[(species, sex)]["lengths"]) / len(data[(species, sex)]["lengths"])
        avg_depth  = sum(data[(species, sex)]["depths"])  / len(data[(species, sex)]["depths"])
        count = len(data[(species, sex)]["lengths"])
        result.append((species, sex, round(avg_length, 2), round(avg_depth, 2), count))
    return result


# Finds percentage of penguins above median ratio by island and species

def ratio_above_species_median_pct(rows):

    species_ratios = {}

    # A) Find the median for each species.

    for r in rows:
        sp = r.get("species", "")
        bl = to_float(r.get("bill_length_mm", ""))
        bd = to_float(r.get("bill_depth_mm", ""))
        if bl is None or bd is None or bd == 0:
            continue
        ratio = bl / bd
        if sp not in species_ratios:
            species_ratios[sp] = []
        species_ratios[sp].append(ratio)

    species_median = {}
    for sp, vals in species_ratios.items():
        if vals:
            species_median[sp] = statistics.median(vals)


    # B) Calculate the proportion of each (island, species) above the median.

    counts = {}
    above = {}
    
    for r in rows:
        island = r.get("island", "")
        sp = r.get("species", "")
        if sp not in species_median:
            continue

        bl = to_float(r.get("bill_length_mm", ""))
        bd = to_float(r.get("bill_depth_mm", ""))
        if bl is None or bd is None or bd == 0:
            continue

        ratio = bl / bd
        key = (island, sp)
        counts[key] = counts.get(key, 0) + 1
        if ratio > species_median[sp]:
            above[key] = above.get(key, 0) + 1

    result = []
    for key in counts:
        island, sp = key
        total = counts[key]
        high = above.get(key, 0)
        pct = round(100 * high / total, 2) if total else 0.0
        result.append((island, sp, pct))
    return result


# Writes calculation results into CSV files

def write_avg_results(filename, results):
   

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["species", "sex", "avg_bill_length_mm", "avg_bill_depth_mm", "count"])
        for item in results:
            writer.writerow(item)


# Test Functions

if __name__ == "__main__":
    data = load_data("penguins.csv")
    print("Total number of rows:", len(data))
    print("First two rows:")
    print(data[:2])

    avg_results = avg_bill_by_species_sex(data)
    print("\nExample of average bill length and depth by species and sex:")
    for item in avg_results[:3]:
        print(item)

    ratio_results = ratio_above_species_median_pct(data)
    print("\nExample of percentage of bill ratio above species median:")
    for item in ratio_results[:3]:
        print(item)

    # Write results to a CSV file
    write_avg_results("avg_results.csv", avg_results)
    print("\navg_results.csv has been successfully written.")