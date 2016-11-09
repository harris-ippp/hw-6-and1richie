#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

resp = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General")

soup = bs(resp.content, 'html.parser')

ls = soup.find_all("tr", "election_item")

with open("ELECTION_ID","w") as output:
    for line in ls:
        output.write(line.find("td",'year first').string + " " + \
        line.get('id').split('-')[2] + "\n")
