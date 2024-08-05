# -*- coding: utf-8 -*-
"""
Created on Aug 2024
@author: Wiebe Nijland w.nijland@uu.nl
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

os.chdir('C:/Temp/data2')

rawdata = pd.read_csv("./RawData/etmgeg_260.txt", skiprows=51, skipinitialspace=True)
rawdata.head()
rawdata.describe()
rawdata.info()

data = pd.DataFrame(
    { 
     "date" : pd.to_datetime(rawdata['YYYYMMDD'], format='%Y%m%d'),
     "precip_mm" : rawdata['RH'] * 0.1, 
     "potEvap_mm" : rawdata['EV24'] * 0.1,
     "Tmean_degC" : rawdata['TG'] * 0.1,
     } )

# fix negative values in precip (-1 is used to indicate values < 0.5 instead of 0 in original dataset)
data.info()
data.loc[data["precip_mm"] < 0.0, "precip_mm"] = 0.0
data.info()



