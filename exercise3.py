#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:57:19 2023

@author: macbookpro
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

market_capitalization = np.array([33367, 68785, 20979, 29741])
companies = ["Barclays", "BP", "Tesco", "Vodaphone"]

plt.figure()
plt.pie(market_capitalization, labels=companies)
plt.title("Market Capitalization of Four Companies")
plt.show()

plt.figure()
market_capitalization_fraction = market_capitalization/1814000
plt.pie(market_capitalization_fraction, labels=companies, normalize=False)
plt.title("Market Capitalization Fraction of Four Companies")
plt.show()

plt.figure()
plt.bar(companies, height=market_capitalization, width=0.8)
plt.show()

vod_ann = pd.read_csv("VOD_ann.csv")
bp_ann = pd.read_csv("BP_ann.csv")
tsco_ann = pd.read_csv("TSCO_ann.csv")
bcs_ann = pd.read_csv("BCS_ann.csv")
print(vod_ann)
