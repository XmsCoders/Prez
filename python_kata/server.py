#!/usr/bin/python
import BaseHTTPServer
import json

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        jsonObject = json.loads(post_body)
        print jsonObject

        team = jsonObject["team"]
        print "New request from " + team+" team (" +self.client_address[0]+")"
        if team in hasPlayed:
            print "But already submitted..."
            self.wfile.write("Sorry, You have already submitted...")
            return
        hasPlayed[team]=True

        map = jsonObject["map"]
        x_length=len(map[0])
        y_length=len(map)

        miner = jsonObject["miner"]
        exit = jsonObject["exit"]
        escapePlan = jsonObject["escape_plan"]

        result=checkResultFunc(map, miner, exit, escapePlan, x_length, y_length)

        if result!=-1:
            print team+" team succeded with "+str(result)+" moves"
            self.wfile.write("SUCCESS, YOUR MINOR REACHED THE EXIT with "+str(result)+" moves")
        else:
            print team+" team failed"
            self.wfile.write("YOUR MINOR DID NOT REACH THE EXIT")
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('<html><body>Use POST with following json structure in raw body :<br/><br/>'
                         '{"team":"blue",<br/>          "map" : [[true, false],<br/>          [true, true ],<br/>          [true, false]],<br/>"miner" : {"x":0, "y":0},<br/>"exit" : {"x":1, "y":1},<br/>"escape_plan" : ["down", "down", "right", "left"]<br/>}'
                         '</body></html>')
        return

def checkResultFunc(map, miner, exit, escapePlan, x_length, y_length):
    for idx in range(0,len(escapePlan)):
        nextMove=escapePlan[idx]
        miner=getNextPosition(miner, nextMove, x_length, y_length)
        print "New miner position" + json.dumps(miner)
        if map[miner["y"]][miner["x"]] == False:
            return -1
        if miner["x"]==exit["x"] and miner["y"]==exit["y"]:
            return idx+1
    return -1

def getNextPosition(actualPosition, move, x_length, y_length):
    if move=="down" and actualPosition["y"]+1<y_length:
        return {"y":(actualPosition["y"]+1), "x":actualPosition["x"]}
    elif move=="up" and actualPosition["y"]>0:
        return {"y":(actualPosition["y"]-1), "x":actualPosition["x"]}
    elif move=="left" and actualPosition["x"]>0:
        return {"y":actualPosition["y"], "x":(actualPosition["x"]-1)}
    elif move=="right" and actualPosition["x"]+1<x_length:
        return {"y":actualPosition["y"], "x":(actualPosition["x"]+1)}
    return actualPosition

hasPlayed={}

 #   =dict({"white":False, "blue":False, "green":False, "yellow":False})
print "Listening on port 8080..."
server = BaseHTTPServer.HTTPServer(('', 8080), MyHandler)
server.serve_forever()
