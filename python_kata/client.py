#!/usr/bin/python

import requests
import json

## game parameters ##
map = [[True, False],
       [True, True ],
       [True, False]]
miner= {"x":0, "y":0}
exit={"x":1, "y":1}
## End Of game parameters ##

my_team="brown"

def solve(map, miner, exit):
    escape_plan=["down", "right"]
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


