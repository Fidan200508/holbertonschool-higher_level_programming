import csv
import json
import os.path


def convert_csv_to_json(csv_file):
    if not os.path.exists(csv_file):
       print("file not found")
       return False
    with open(csv_file, newline="") as f:
        read = csv.DictReader(f)
        data = list(read)


    with open("data.json", "w") as json_file:
        json.dump(data, json_file)
        return True
