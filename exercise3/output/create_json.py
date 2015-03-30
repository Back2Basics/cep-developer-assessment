# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 08:53:39 2015

@author: Jeremy Langley
"""

import pandas as pd
import ujson as json

mean_csv='../input/mean.csv'
pct_csv='../input/pct.csv'
stats_csv='../input/stats.csv'
ofile = '../output/something.json'

mean_df = pd.read_csv(mean_csv)
pct_df = pd.read_csv(pct_csv)
stats_df = pd.read_csv(stats_csv)
stats_df_munge = stats_df.ix[3:,'fldimp':'impsust']

question_list= ['fldimp','undrfld','advknow','pubpol','comimp','undrwr','undrsoc','orgimp','impsust']

survey = {}
for x in range(1, stats_df_munge.ix[:,'fldimp':'impsust'].shape[1]):
	question = {}
	question['cohorts']=[]
	question['past_results']=[]
	question['segmentations']=[]
	question['type']='percentileChart'

	current = {}
	current['name']="2014"
	current['value']=mean_df[x]
	current['percentage']=pct_df[x]
	question['current']=current

	absolutes = []
	for i in question_list:
		absolutes.append(list(stats_df_munge[i]))
	question['absolutes']=absolutes

	survey[question_list[x]]=question

reports={"elements": question, "segmentations": [], "cohorts": [], "name": "Tremont 14S Report", "title": "Tremont 14S Report"}
output = {"version": "1.0",  "reports": [reports]}
#print output_dict

with open('../output/test.json', 'w') as outfile:
	json.dump(output, ofile)