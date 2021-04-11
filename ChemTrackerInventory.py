# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:47:44 2021

@author: adple
"""

#Things to know from inventory - future updates
#- if anything is out of place/missing
#- if we need to order anything
#- general overview (total number of containers in each location and change in value)
#- new chemicals added to inventory
#- chemical removed from inventory

#%% import inventory data and manipulate
#import packages
import pandas as pd
from datetime import date

#import data
filedate = date.today().strftime('%#m-%d-%Y')
filepath = 'C:\\Users\\adple\\Desktop\\DataScience\\' + filedate + '-Chemical_Container_export.csv'
inventory = pd.read_csv(filepath)

#calculate total number of containers
current_totals = inventory['Chemical Name'].value_counts()
current_totals = current_totals.rename_axis('Chemical Name').to_frame('Counts').reset_index()

#compare to required totals
required_totals = pd.read_csv('C:\\Users\\adple\\Desktop\\DataScience\\InventoryRequiredTotals.csv')
totals = required_totals.merge(current_totals, on = 'Chemical Name')
order = totals[totals['Counts'] < totals['Minimum']]

#%%send email
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Chemical Inventory has been completed

The following chemicals need to be ordered:
    """+order.to_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)