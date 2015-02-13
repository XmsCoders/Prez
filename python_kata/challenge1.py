#!/usr/bin/python

import requests
import json

## Game variables ##
map = [[True, False, True, True, True, False, True],
       [True, True, True, False, True, True, True]]
miner= {"x":0, "y":0}
exit={"x":6, "y":0}
my_team="brown"
## End Of Game variables ##


def solve(map, miner, exit):
    escape_plan=["down", "right", "right", "up",  "right", "right", "down", "right", "right", "up"]
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


