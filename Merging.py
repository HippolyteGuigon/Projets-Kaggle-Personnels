import pandas as pd 
import numpy as np

df_train = pd.read_csv("train.csv")
holidays = pd.read_csv("holidays_events.csv")
stores = pd.read_csv("stores.csv")
transaction = pd.read_csv("transactions.csv")
test = pd.read_csv("test.csv")


def merging():
    df_train_merged = df_train.merge(holidays, on="date", how="left")
    df_train_merged = df_train_merged.merge(transaction, on=["date","store_nbr"] , how="left")
    return df_train_merged