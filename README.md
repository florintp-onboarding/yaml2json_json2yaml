# Convert yaml2json and json2yaml files using Python

This repository provide basic Python tools to convert YAML to JSON or JSON to YAML files. It was tested on Python3 with regular config files (YAML).

# Requirements
- Python 3
- JQ

# Python Libraries
- PIP
- pyyaml
- datetime

# How to use the tools

- Install prerequisites
````
pip install pyyaml
python3.11 -m pip install --upgrade pip
````

- Execute the convert tool YAML->JSON
````
python3 yaml2json.py config.yaml
````

- Execute the convert tool JSON->YAML
````
python3 json2yaml.py config.json
````

# Output Example
a) Successful conversion of an YAML file named `config` into `config.json`:
````
# python3 yaml2json.py config
[2024-02-13 23:36:19.302335]-[WARNING]-Filename 'config' does not have an extension...
[2024-02-13 23:36:19.302365]-[INFO]-Start conversion of file: config
[2024-02-13 23:36:19.305910]-[INFO]-Done conversion of file: config into file: config.json
````

b) Failure to convert an YAML `config` file if the output file `config.json` is already present in the current directory:
````
# python3 yaml2json.py config
[2024-02-13 23:34:17.911103]-[WARNING]-Filename 'config' does not have an extension...
[2024-02-13 23:34:17.911127]-[ERROR]-Conversion was NOT performed as the output file 'config.json' is already present!
````

c) Failure to convert an YAML `config` file if the format is not YAML:
````
# python3 json2yaml.py config
[2024-02-13 23:37:06.350182]-[WARNING]-Filename 'config' does not have an extension...
[2024-02-13 23:37:06.350216]-[INFO]-Start conversion of file: config
[2024-02-13 23:37:06.350510]-[ERROR]-Could not convert the 'config' into 'config.yaml'! (Wrong format?)
````
