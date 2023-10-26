import pandas as pd

data = pd.read_csv("./2004-2021.tsv", sep=",")
data_sem_duplicata = data.drop_duplicates()

"""O método fillna() pode ser aplicado nas seguintes colunas: 
'PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA', 'PREÇO MÍNIMO REVENDA' e 'PREÇO MÁXIMO REVENDA'"""

media_preco_medio_revenda = data_sem_duplicata['PREÇO MÉDIO REVENDA'].mean()
media_desvio_padrao_revenda = data_sem_duplicata['DESVIO PADRÃO REVENDA'].mean()
media_preco_minimo_revenda = data_sem_duplicata['PREÇO MÍNIMO REVENDA'].mean()
media_preco_maximo_revenda = data_sem_duplicata['PREÇO MÁXIMO REVENDA'].mean()

data_sem_duplicata['PREÇO MÉDIO REVENDA'] = data_sem_duplicata['PREÇO MÉDIO REVENDA'].fillna(media_preco_medio_revenda)
data_sem_duplicata['DESVIO PADRÃO REVENDA'] = data_sem_duplicata['DESVIO PADRÃO REVENDA'].fillna(media_desvio_padrao_revenda)
data_sem_duplicata['PREÇO MÍNIMO REVENDA'] = data_sem_duplicata['PREÇO MÍNIMO REVENDA'].fillna(media_preco_minimo_revenda)
data_sem_duplicata['PREÇO MÁXIMO REVENDA'] = data_sem_duplicata['PREÇO MÁXIMO REVENDA'].fillna(media_preco_maximo_revenda)


print("\nMÉTODO HEAD() SEM DUPLICATAS:\n", data_sem_duplicata.head())
print("\nMÉTODO INFO() SEM DUPLICATAS:\n", data_sem_duplicata.info())
print("\nMÉTODO DESCRIBE() SEM DUPLICATAS:\n", data_sem_duplicata.describe())

cleaned_data = data_sem_duplicata.to_csv('./dados_limpos.csv', sep="\t")