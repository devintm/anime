%cpaste

import pandas as pd
import datetime

df = pd.read_csv('data1/finalanime1.zip', usecols=["anime_id", "name"])
items = pd.read_csv("items1.csv")

def item_maker(x, n):
    for item in items.sort_values(by=x, ascending=False).name[n:]:
        return item

def dmf(x,n):
    try:
        return item_maker(x,n)
    except:
        return 0

df = df.head()

start_time = datetime.datetime.now()
df["one"] = df.apply(lambda x: dmf(x["name"], 1), axis=1)                                                                               
end_time = datetime.datetime.now()

total_time = (end_time - start_time).total_seconds()
print(total_time)
