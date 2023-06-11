#!/usr/bin/env python
# coding: utf-8

#1. Import data and libaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("dataset.csv")

#2. Select data to plot
category_age = data.loc[:, ["category", "year", "birth_date"]]
category_age.columns = ["category", "win_year", "birth_date"]

#3. Clean and transform data
category_age.dropna(inplace = True)
category_age["birth_date"] = pd.to_datetime(category_age["birth_date"])
category_age["birth_year"] = category_age["birth_date"].dt.year
category_age["winner_age"] = category_age["win_year"] - category_age["birth_year"].astype(int)

category_age["decade"] = pd.cut(category_age["win_year"],
                                bins = range(1900, 2030, 10),
                                labels = range(1900, 2020, 10))

category_age = category_age.groupby(["category", "decade"]).mean("winner_age").reset_index()
category_age = category_age.pivot(index = "decade", columns = "category", values = "winner_age")

#4. Plot data
fig, ax = plt.subplots(figsize = (12, 8))

colors = ["red", "green", "orange", "blue", "purple", "magenta"]
category_age.plot(ax = ax, color = colors)

ax.set_xlabel("Decade")
ax.set_ylabel("Age")
ax.set_title("Nobel-Prize-Winner Average Age (when Received the Prize) by Category over Decades")
ax.legend()
ax.grid(True)
