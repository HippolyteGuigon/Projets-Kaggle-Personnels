import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
from Merging import *

#On commence par une fonction permettant de plotter au cours du temps l'évolution des ventes

df_train_merged = merging()

df_train_merged.date = pd.to_datetime(df_train_merged.date)

#On regarde par regarder, pour une fréquence donnée, la moyenne des ventes

def plotting(frequency):
    frequency = str(frequency)
    plt.figure(figsize=(12, 12))
    plt.title("Average weekly sales over the {}".format(frequency), fontsize=15)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Average sales", fontsize=15)
    plt.plot(df_train_merged.set_index(df_train_merged["date"]).resample(frequency).mean().sales);
    
    
def plot_produit():
    #On regarde ensuite en fonction des produits 
    pd.DataFrame(df_train_merged.groupby("family").sales.mean().sort_values(ascending=False)).plot(kind="bar", figsize=(12, 12), title="Average sales by category");
     

       