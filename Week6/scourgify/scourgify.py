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
        with open(sys.argv[1]) as file:
            reader = csv.reader(file, delimiter=",")
            headers = next(reader)
            
            