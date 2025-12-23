import pandas as pd #to create datframe
import seaborn as sns

# write a function to load the dataset from seaborn
# and return as pandas dataframe

def load_data():
    """load the tips dataset from seaborn and return as pandas dataframe"""
    df=sns.load_dataset("tips")
    return df