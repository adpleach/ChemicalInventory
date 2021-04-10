# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:47:44 2021

@author: adple
"""

#Important things to know from inventory 
#- if anything is out of place/missing
#- if we need to order anything
#- general overview (total number of containers in each location and change in value)
#- new chemicals added to inventory
#- chemical removed from inventory

import pandas as pd

inventory = pd.read_csv(r'C:\filepath\2-16-2021-Chemical_Container_export.csv')

print(inventory.info())

print(inventory['Container Status'])