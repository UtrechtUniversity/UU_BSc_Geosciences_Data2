#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:22:19 2024

@author: niko
"""

import pandas as pd

Q = pd.read_csv("../RawData/Rhine_total.txt")
Q["date"] = pd.to_datetime(Q['date'], format='%Y-%m-%d')
Q = Q.set_index("date")
Q = Q.resample("D").mean()

Q.to_csv("../Data/dailyDischarge.csv")

