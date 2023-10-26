import pandas as pd

from google.cloud import storage

df = pd.read_csv("cadastro.csv")

bucket = storage.Client().bucket("empresa-388100-dados")

blob = bucket.blob("raw/cadastro.csv")

blob.upload_from_string(df.to_csv(index=False), "text/csv")


""" import pandas as pd
from google.cloud import storage
df = pd.read_csv("gs://alphaedtech-exemplos/raw/usuarios.csv")
df.dropna(subset=["cidade"], inplace=True)
idade_media = df.idade.mean()
df.idade = df.idade.fillna(idade_media)
bucket = storage.Client().bucket("alphaedtech-exemplos")
blob = bucket.blob("curated/usuarios.csv")
blob.upload_from_string(df.to_csv(index=False), "text/csv") """
