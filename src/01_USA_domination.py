#!/usr/bin/env python
# coding: utf-8

#1. Import libraries and set up
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick

#2. Import data
data = pd.read_csv("dataset.csv")

#3. Clean and transform data
countries = data["birth_country"].sort_values().unique()

data["decade"] = pd.cut(data["year"],
                        bins = range(1900, 2030, 10),
                        labels = range(1900, 2020, 10))

data.loc[data["birth_country"] != 'United States of America', "birth_country"] = "other countries"

country_winner = data.loc[:, ["decade", "birth_country"]]
country_winner = country_winner.groupby(["decade", "birth_country"]).size()

proportions = country_winner.groupby(level=0, group_keys = False).apply(lambda x: x / float(x.sum()))
proportions = proportions.reset_index(name = "country_prop")
proportions["country_prop"] = proportions["country_prop"] * 100
proportions_pivot = proportions.pivot(index="decade", columns="birth_country", values="country_prop")

#4. Plot data using 100% stacked are chart
fig, ax = plt.subplots(figsize = (12, 8))
ax.stackplot(proportions_pivot.index,
             proportions_pivot["United States of America"],
             proportions_pivot["other countries"],
             labels = ["USA", "Other countries"],
            colors = ["green", "lightgrey"])

# set y-axis formatter to percentage
y_fmt = mtick.PercentFormatter()
ax.yaxis.set_major_formatter(y_fmt)

ax.legend(loc = "upper left")
ax.set_title("The proportion of Nobel-Prize-Winners based on their Birth Country over Time")
ax.grid(True, color ="w")

