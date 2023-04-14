# PROJETO DE CRIAÇÃO DE TABELA EM BANCO DE DADOS COM PYTHON
## GET STARTED

- Crie um banco de dados no PostgreSQL (Ver arquivo PSQL.cmd) (terminal psql):
```
CREATE TABLE my_database;
```

- Crie um arquivo chamado ".env" com os valores das variáveis de ambiente:
```
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=seu_banco_de_dados
DB_USER=postgres
DB_PASSWORD=
```

- Crie um ambiente virtual e instale as dependências (terminal bash):
```
cd "path/to/Atividade_02_connection_python_postgres"
```
```
virtualenv venv 
```
```
source venv/Scripts/activate
```
```
pip install -r requirements.txt
```

- Rode a aplicação (terminal bash):
```
python ./__main__.py
```