#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 06:37:54 2025

@author: kingsleylee
"""

# Association Rule Learning (using Apriori)



# Import required packages

from apyori import apriori
import pandas as pd


# import data


# import

alcohol_transactions = pd.read_csv("data/sample_data_apriori.csv")


# Drop ID column

alcohol_transactions.drop("transaction_id", axis = 1, inplace = True)


# Modify data for apriori algorithm

transactions_list = []

for index, row in alcohol_transactions.iterrows():
    transaction = list(row.dropna())
    transactions_list.append(transaction)

transactions_list

# Apply the Aprior algorithm

apriori_rules = apriori(transactions_list,
                        min_support = 0.003,
                        min_confidence = 0.2,
                        min_lift = 3,
                        min_length = 2, 
                        max_length = 2)


apriori_rules = list(apriori_rules)


apriori_rules[0]


# Convert output to DataFrame

# apriori_rules[0][2][0][0] -- eg. this is how to get down to the information we want from the list

product1 = [list(rule[2][0][0])[0] for rule in apriori_rules]
product2 = [list(rule[2][0][1])[0] for rule in apriori_rules]
support = [rule[1] for rule in apriori_rules]
confidence = [rule[2][0][2] for rule in apriori_rules]
lift = [rule[2][0][3] for rule in apriori_rules]

apriori_rules_df = pd.DataFrame({"product1" : product1,
                                "product2" : product2,
                                "support" : support, 
                                "confidence" : confidence,
                                "lift" : lift})


# Sort rules by descending lift

apriori_rules_df.sort_values(by = "lift", ascending = False, inplace = True)


# Search rules

apriori_rules_df[apriori_rules_df["product1"].str.contains("New Zealand")]




































