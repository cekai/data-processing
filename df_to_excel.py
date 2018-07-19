import pandas as pd
import numpy as np

x_raw = np.load("x_raw_v4.npy")
cats = np.load("x_raw_categories_v4.npy")
preds_cats = np.load("preds_categories.npy")

data = pd.DataFrame(columns=['x','true_category','predicted_category'])

for i in range(len(x_raw)):
    data.loc[i] = [x_raw[i], cats[i], preds_cats[i]]
    
filepath = 'predictions_001.xlsx'

data.to_excel(filepath, index=False)
