#!/usr/local/bin/python3

import sys
import yaml
import json
with open("all.yaml", 'r') as yaml_in:
    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
    json.dump(yaml_object, sys.stdout)
