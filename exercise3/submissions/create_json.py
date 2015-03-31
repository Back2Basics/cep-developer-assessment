# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 08:53:39 2015

@author: Jeremy Langley

Create a json report for customer who's name and ID number are listed in 
report_name and customer_no
based on information in mean.csv, pct.csv and stats.csv
"""

import pandas as pd
import ujson as json
import pprint

customer_no = 8
report_name= "Tremont 14S Report"

mean_csv='../input/mean.csv'
pct_csv='../input/pct.csv'
stats_csv='../input/stats.csv'
ofile = '../output/output.json'

mean_df = pd.read_csv(mean_csv)
pct_df = pd.read_csv(pct_csv)
stats_df = pd.read_csv(stats_csv)
stats_df_munge = stats_df.ix[3:,'fldimp':'impsust']

survey = {}
for x in stats_df.columns[1:]:
	question = {}
	question['type']='percentileChart'
	question['absolutes']=stats_df_munge[x].to_json(orient="values")

	current = {}
	current['name']="2014"
	current['value']=mean_df[x][customer_no]
	current['percentage']=pct_df[x][customer_no]
	question['current']=current

	question['cohorts']=[]
	question['past_results']=[]
	question['segmentations']=[]

	survey[x]=question

more_data={"name": report_name, 
            "title": report_name,
            "cohorts": [],            
            "segmentations": [],
            "elements": survey}
output = {"version": "1.0",  "reports": [more_data]}

with open(ofile, 'w') as outfile:
    pprint.pprint(output, stream=outfile)
    
    