import pandas as pd
import numpy as np
df = pd.read_excel("udemy.xlsx",header=0)
print(df.shape)

print("Tüm Dataframe")
print(df)
print("Ders Adı sütunu")
print(df["Ders Adı"])

input("Devam etmek için enter'a basın.")
print("Videoların toplam saati 50'den fazla olan dersleri filtreleyeceğiz.")
print(df.index)
filtreSonuclari = df.sort_values(by='Videoların toplam saati', ascending=False).head(10)
print(filtreSonuclari)

df.to_excel("udemyfiltre.xlsx")
print("Excel dosyasına yazıldı. ")
