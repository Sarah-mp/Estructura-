import pandas as pd

df = pd.read_csv("spam.csv")

df['etiqueta'] = df['Category'].map({'ham': 0, 'spam': 1})

print(df.head())




