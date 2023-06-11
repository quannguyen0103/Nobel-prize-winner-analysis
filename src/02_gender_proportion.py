#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#1. Import dataset
data = pd.read_csv("dataset.csv")

#2. Clean and transform data
gender = data.groupby("sex").size().reset_index(name = "number")
total_gender = data["sex"].count()
gender_prop = gender["number"]/total_gender

#3. Plot the data
labels = ["Female", "Male"]
colors = ["lightgrey", "darkorange"]

plt.pie(gender_prop,
       labels = labels,
       autopct='%1.1f%%',
       colors = colors,
       startangle = 90)

plt.title("Nobel-Prize-Winner gender proportion")
