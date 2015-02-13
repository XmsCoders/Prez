#!/usr/bin/python

import requests
import json

## Game variables ##
map = [[True, True, True, False],
       [True, False, True, True],
       [True, False, True, True],
       [True, True, False, False],
       [False, True, False, True],
       [True, True, True, True]]
miner= {"x":2, "y":2}
exit={"x":3, "y":4}
my_team="brown"
## End Of Game variables ##


def solve(map, miner, exit):
    escape_plan=["up", "up", "left", "left", "down", "down", "down", "right", "down", "down", "right", "right", "up"]
    escape_plan=["right","up", "left", "up", "left", "left", "down", "down", "down", "right", "down", "down", "right", "right", "up"]
    # [...]
    return escape_plan

escape_plan=solve(map, miner, exit)

post_data = dict({"team":my_team,
"map" : map,
"miner" : miner,
"exit" : exit,
"escape_plan" : escape_plan
})

post_response = requests.post(url='http://localhost:8080', data=json.dumps(post_data))
print post_response.content


