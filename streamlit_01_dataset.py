# import library
import numpy as np
import pandas as pd

# func get_dataset
def get_dataset():
  
  # load dataset
  dataset = pd.read_csv("dataset/nike-sales-dataset_v2.csv")
  
  # return values
  return dataset