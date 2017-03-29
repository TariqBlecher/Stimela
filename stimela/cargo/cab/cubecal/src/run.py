import sys
import os
import json

sys.path.append("/utils")
import utils

CONFIG = os.environ["CONFIG"]
INPUT = os.environ["INPUT"]
OUTPUT = os.environ["OUTPUT"]
MSDIR = os.environ["MSDIR"]

cab = utils.readJson(CONFIG)

params = cab["parameters"]

pos_args = ["msname", "smname"]
pos_cmd = []
for arg in pos_args:
    param = filter(lambda a: a['name']==arg, params)[0]
    value = param['value']
    params.remove(param)

    if value:
        pos_cmd.append(value)

args = {}
for param in cab['parameters']:
    name = param['name']
    value = param['value']

    if value is None:
        continue

    args[name] = value

cmd = []

for arg, value in args.items():
    cmd.append("--" + arg)
    cmd.append(value)

ARGS = cmd + pos_cmd

utils.xrun(cab['binary'], ARGS)
