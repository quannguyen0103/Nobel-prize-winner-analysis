#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. import libraries and data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data
data = pd.read_csv("dataset.csv")


# In[4]:


#2. clean and transform data
data["birth_date"] = pd.to_datetime(data["birth_date"])
data["birth_year"] = data["birth_date"].dt.year
data["win_prize_age"] = data["year"].astype(int) - data["birth_year"].astype(int)
data = data.dropna(subset=["birth_year"])


# In[5]:


#3. select data to plot
winners = data[["year", "win_prize_age"]]
winners_age = winners.groupby("year").mean().reset_index()
winners_age.columns = ["year","avg_age"]


# In[ ]:


#4. plot the data
fig, ax = plt.subplots(figsize = (12, 8))
ax.plot(winners["year"],
       winners["win_prize_age"],
       linestyle = "None",
       marker = "o",
       markerfacecolor = "green")

ax.set_title("Age of Nobel-Prize-Winner When receiving the Nobel Prize over time")
ax.set_xlabel("Year")
ax.set_ylabel("Age")
ax.grid(True)

