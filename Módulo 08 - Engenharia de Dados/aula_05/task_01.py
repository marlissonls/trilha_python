import pandas as pd

# Primeiro arquivo: Balanço anual

ann_balance = pd.read_csv("./annual-balance-2007-2021.csv")
ann_balance_sem_duplicata = ann_balance.drop_duplicates()

ann_balance_sem_nan = ann_balance_sem_duplicata.dropna(subset="Period")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="Inst_sector")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="Inst_sector_code")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="Descriptor")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="SNA08TRANS")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="Asset_liability_code")
ann_balance_sem_nan = ann_balance_sem_nan.dropna(subset="Values")

print("\nMÉTODO HEAD() SEM DUPLICATAS:\n\n", ann_balance_sem_nan.head())
print("\nMÉTODO INFO() SEM DUPLICATAS:\n") 
ann_balance_sem_nan.info()
print("\nMÉTODO DESCRIBE() SEM DUPLICATAS:\n\n", ann_balance_sem_nan.describe())

ann_balance_sem_nan.to_csv('./annual-balance-2007-2021_limpos.csv')


# Segundo arquivo: Enquete anual

ann_survey = pd.read_csv("./annual-enterprise-survey-2021.csv")
ann_survey_sem_duplicata = ann_survey.drop_duplicates()

ann_survey_sem_nan = ann_survey_sem_duplicata.dropna(subset="year")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="industry_code_ANZSIC")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="industry_name_ANZSIC")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="rme_size_grp")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="variable")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="value")
ann_survey_sem_nan = ann_survey_sem_nan.dropna(subset="unit")

print("\nMÉTODO HEAD() SEM DUPLICATAS:\n\n", ann_survey_sem_nan.head())
print("\nMÉTODO INFO() SEM DUPLICATAS:\n")
ann_survey_sem_nan.info()
print("\nMÉTODO DESCRIBE() SEM DUPLICATAS:\n\n", ann_survey_sem_nan.describe())

ann_survey_sem_nan.to_csv('./annual-enterprise-survey-2021_limpos.csv')