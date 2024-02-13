import datetime
import yaml
import json
import sys
import os

if int(len(sys.argv)) < 2:
    print(f"[%s]-[ERROR]-No files to convert... number of arguments is {int(len(sys.argv)-1)}!" % datetime.datetime.now())
    sys.exit(1)

filename = sys.argv[1]
new_extension = 'json'

if os.path.isfile(filename):
    if '.' in filename:
        base_name = os.path.splitext(filename)[0]
        newfilename = base_name + '.' + new_extension
    else:
        print(f"[%s]-[WARNING]-Filename '{filename}' does not have an extension..." % datetime.datetime.now())
        newfilename = filename + '.' + "json"

    if os.path.isfile(newfilename):
        print(f"[%s]-[ERROR]-Conversion was NOT performed as the output file '{newfilename}' is already present!" % datetime.datetime.now())
        sys.exit(2)

    try:
        print(f"[%s]-[INFO]-Start conversion of file: {filename}" % datetime.datetime.now())
        with open(filename, 'r') as file:
            configuration = yaml.safe_load(file)
        with open(newfilename, 'w') as json_file:
             json.dump(configuration, json_file)
        #with open(newfilename, 'r') as json_file:
        #    print(json_file.read())
        print(f"[%s]-[INFO]-Done conversion of file: {filename} into file: {newfilename}" % datetime.datetime.now())

    except Exception as e:
        print(f"[%s]-[ERROR]-Could not convert the '{filename}' into '{newfilename}'! (Wrong format?)" % datetime.datetime.now())
        sys.exit(1)

else:
    print(f"[%s]-[ERROR]-Filename '{filename}' not found!" % datetime.datetime.now())
    sys.exit(1)

