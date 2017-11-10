# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:51:23 2017

@author: zhang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#prepare the treasury yield rate data from 1/2/1996 to 11/21/2016 and drop the 1 month yeild rate 
df_origin=pd.read_csv('C:\\Users\\zhang\\Desktop\\Treasury_Yield_Curve.csv')
df_origin.index=df_origin['Date']
df_cut=df_origin.drop(['Date','1 mo'],axis=1)
df_cut=df_cut.loc['1/2/1996':'11/21/2016',:]

#calculate daily difference
df_differ=df_cut-df_cut.shift(1)

#calculate correlation and vol of level data 
cut_cor=df_cut.corr()
cut_vol=df_cut.std(axis=0)

#calculate correlation and vol of daily difference data 
differ_cor=df_differ.corr()
differ_vol=df_differ.std(axis=0)

#plot the vol curve of level data & difference data
cut_vol.plot(ylim=(-3.0,3),color='orange',legend=True,label='volatility of level data')
plt.show()

differ_vol.plot(ylim=(-3.0,3),color='g',legend=True,label='volatility of daily differences')
plt.show()




