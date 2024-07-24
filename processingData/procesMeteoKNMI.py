# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file to process raw daily precip meteo from the KNMI.
"""

import pandas as pd

data = pd.read_csv("../RawData/etmgeg_260.txt", skiprows=51)
dates = pd.to_datetime(data['YYYYMMDD'], format='%Y%m%d')

P = pd.to_numeric(data['   RH'], errors='coerce')
P[P<0.0] = 0.0
P = P * 0.1
E = pd.to_numeric(data[' EV24'], errors='coerce')
E = E * 0.1

Tas = pd.to_numeric(data['   TG'], errors='coerce')
Tas = Tas * 0.1

P = P.to_frame()
P = P.set_index(dates)
P = P.rename(columns={"   RH":"Precip"})
annualP = P.resample("YE").sum()
annualP.index = annualP.index.strftime('%Y')
annualP.index.names = ['Year']
annualP[5:-1:].to_csv("../Data/annualPrecipitation.csv")
P.index.names = ['Date']
P.to_csv("../Data/dailyPrecipitation.csv")

E = E.to_frame()
E = E.set_index(dates)
E = E.rename(columns={' EV24':"Evap"})
annualE = E.resample("YE").sum()
annualE.index = annualE.index.strftime('%Y')
annualE.index.names = ['Year']
annualE[57:-1:].to_csv("../Data/annualEvaporation.csv")
E.index.names = ['Date']
E.to_csv("../Data/dailyEvaporation.csv")

Tas = Tas.to_frame()
Tas = Tas.set_index(dates)
Tas = Tas.rename(columns={'   TG':"Tas"})
Tas.index.names = ['Date']
Tas.to_csv("../Data/dailyTemperature.csv")