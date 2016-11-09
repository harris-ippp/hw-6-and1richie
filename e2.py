#!/usr/bin/env python

import requests

for line in open("ELECTION_ID"):
    year = line.split(" ")[0]
    electionID = line.split(" ")[1].strip()
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(electionID)
    resp = requests.get(addr)
    file_name = year + ".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
