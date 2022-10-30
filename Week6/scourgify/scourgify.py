import csv
from os import path
import os.path
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 3:
    extensionCheck = sys.argv[1].split(".")[-1]
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif extensionCheck == "csv" and not path.exists(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        output = []
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                splitName = row["name"].split(",")
                output.append({'first': splitName[1].lstrip(), 'last': splitName[0], 'house':row["house"]})
        
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in output:
                writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
            