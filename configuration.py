import json

with open('config.json', mode='r') as f:
    configs = json.load(f)

try:
    grid_size = configs['grid_size']
except KeyError:
    grid_size = None

try:
    block_size = configs['block_size']
except KeyError:
    block_size = 10
