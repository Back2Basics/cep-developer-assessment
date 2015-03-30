# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:40:45 2015

@author: Jeremy Langley

Takes '../input/xl.csv' as input
sets unnecessary values as NaN
Produces descriptive statistics of the client ratings
Outputs mean values to '../output/mean.csv'
Outputs descriptions to '../output/stats.csv'

"""

import pandas as pd
import numpy as np

survey = pd.read_csv('../input/xl.csv')
survey.replace([77,88], np.nan, inplace=True)

results = survey[survey.notnull()].groupby('fdntext').mean()

results.ix[:,'fldimp':'impsust'].to_csv('../output/mean.csv')
results.ix[:,'fldimp':'impsust'].describe().to_csv('../output/stats.csv')
