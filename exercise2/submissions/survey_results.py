# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 7:49:13 2015

@author: Jeremy Langley

Takes ../input/mean.csv as input
Using percentileofscore this finds 
the Percentile of each client rating within each column.

Outputs to ../output/pct.csv
"""
import pandas as pd
from scipy.stats import percentileofscore

ifile = '../input/mean.csv'
ofile = '../output/pct.csv'

def get_percentile(cols):
    output = []
    for x in cols:
        percentile = percentileofscore(cols, x, kind='mean')
        output.append(percentile)
    return output

def main():
    survey = pd.read_csv(ifile)
    survey_data = survey.ix[:,'fldimp':'impsust']
    transform = []
    for x in survey_data:
        cols = get_percentile(survey_data[x])
        transform.append((x, cols))

    survey.ix[:,'fldimp':'impsust']=pd.DataFrame.from_items(transform)
    survey.to_csv(ofile)

main()
