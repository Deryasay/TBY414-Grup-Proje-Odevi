import pandas as pd
import numpy as np
from kmodes.kmodes import KModes

df = pd.read_excel("udemy_2.xlsx",header=0)
print(df.shape)

print("Tum Dataframe")
print(df)

input("Devam etmek icin enter'a basin.")
print(df.index)

km_cao = KModes(n_clusters=2, init = "Cao", n_init = 2, verbose=1)
fitClusters_cao = km_cao.fit_predict(df)
print(fitClusters_cao)
df["Kategori"] = fitClusters_cao

df.to_excel("udemyfiltre_2.xlsx")
print(df)
