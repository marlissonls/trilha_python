import pandas as pd

ann_survey = pd.read_csv("./annual-enterprise-survey-2021_limpos.csv")
ann_balance = pd.read_csv("./annual-balance-2007-2021_limpos.csv")

survey_balance_concat = pd.concat([ann_survey, ann_balance], axis=1)

survey_balance_concat.info()

survey_balance_concat.to_csv("survey_balance_concat.csv")