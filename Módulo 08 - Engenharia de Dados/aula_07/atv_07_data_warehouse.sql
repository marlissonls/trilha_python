--Nesta aula do módulo 7 de Python vamos estudar Data Warehouse

--Crie uma conta na plataforma do Google Cloud Platform (GCP) e acesse o BigQuery; 
--Utilizando o BigQuery, crie um projeto para o exercício; 
--Crie um dataset no projeto; 
--Faça o upload de um conjunto de dados próprio; 
--Realize consultas no BigQuery para responder às seguintes perguntas: 

--a. Qual é a contagem total de registros na tabela? 
SELECT COUNT(*) as total_registros
FROM `basedosdados.br_fbsp_absp.municipio`

--b. Quais são as colunas presentes na tabela? 
SELECT
  column_name,
  data_type
FROM
  `basedosdados.br_fbsp_absp.INFORMATION_SCHEMA.COLUMNS`
WHERE
  table_name = 'municipio'

--c. Faça uma consulta que retorne os 10 primeiros registros da tabela; 
SELECT *
FROM `basedosdados.br_fbsp_absp.municipio`
LIMIT 10

--d. Execute uma consulta que agregue os dados de uma coluna numérica, fornecendo a média, o valor mínimo e o valor máximo; 
SELECT
  AVG(quantidade_homicidio_doloso) AS media,
  MIN(quantidade_homicidio_doloso) AS valor_minimo,
  MAX(quantidade_homicidio_doloso) AS valor_maximo
FROM
  `basedosdados.br_fbsp_absp.municipio`

--e. Faça uma consulta que filtre os registros com base em uma condição específica.
SELECT *
FROM `basedosdados.br_fbsp_absp.municipio`
WHERE quantidade_homicidio_doloso > 1000
LIMIT 20