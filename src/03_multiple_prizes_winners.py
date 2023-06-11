#!/usr/bin/env python
# coding: utf-8

#1. Import library and data
import pandas as pd
data = pd.read_csv("dataset.csv")

#2. Get the list of scientists/writers/activists (names, and job) who win Nobel prize MORE THAN 1.
data["category"].unique()
nobel_winners = data.loc[:, ["category", "full_name"]]
nobel_winners = data.groupby(["full_name", "category"]).size().reset_index(name = "nobel prizes")
names = nobel_winners.loc[nobel_winners["category"].isin(['Chemistry', 'Literature', 'Peace']) 
                          & (nobel_winners["nobel prizes"] > 1)]
