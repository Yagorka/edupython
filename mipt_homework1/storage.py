import os
import tempfile
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description='key-value')
parser.add_argument('--key', type=str, help='keys')
parser.add_argument('--val', type=str, help='values')
args = parser.parse_args()

#print(args.key, args.val)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#print(storage_path) папка C:\Users\Yagor\AppData\Local\Temp\storage.data

# with open(storage_path, 'r') as f:
def to_json(storage_path, key, val):
    if args.val == None:
        with open(storage_path, 'r') as json_file:
            data = json.load(json_file)
            if key in data:
                print(", ".join(data[key]))
            else:
                print("")
            #print(data)

    else:
        with open(storage_path, 'r') as json_file:
            data = json.load(json_file)
            #print(data)
            if key in data:
                data[key].append(val)
            else:
                data[key] = []
                data[key].append(val)
            with open(storage_path, 'w') as json_file_write:
                json.dump(data, json_file_write)


if not os.path.exists(storage_path):
    data2 = {}
    with open(storage_path, 'w') as outfile:
        json.dump(data2, outfile)
to_json(storage_path, args.key, args.val)

