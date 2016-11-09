#!/usr/bin/env python

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

votes = []

for line in open("ELECTION_ID"):
    year = line.split(" ")[0]
    header = pd.read_csv(year + ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(year + ".csv", index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year
    votes.append(df)

for year in range(len(votes)):
    majorVote = pd.concat([votes[year][['Democratic','Republican',\
    'Total Votes Cast','Year']]], axis = 1).head(1)
    majorVote['Republican Vote Share'] = \
    majorVote['Republican']/majorVote['Total Votes Cast']
    if year == 0:
        voteShare = pd.concat([majorVote], axis = 1)
    else:
        voteShare = pd.concat([voteShare, majorVote], axis = 0)
#     break

ax  = voteShare.plot(x = 'Year', y = "Republican Vote Share", \
        title = "President General Election Results in Accomack County, Virginia")

ax.get_figure().savefig('accomack.png')
