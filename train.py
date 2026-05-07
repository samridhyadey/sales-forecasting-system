import pandas as pd
from xgboost import XGBRegressor
import pickle

df = pd.read_excel("data/sales.xlsx")

df['lag_1'] = df['sales'].shift(1)
df = df.dropna()

X = df[['lag_1']]
y = df['sales']

model = XGBRegressor()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))