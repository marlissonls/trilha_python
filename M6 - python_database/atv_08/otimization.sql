CREATE TABLE user_table (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE INDEX name_index ON user_table (name);

CREATE TABLE compare_results (
  requisicao VARCHAR(1),
  quantidade_dados VARCHAR(10),
  tempo_execucao DOUBLE PRECISION
);


DELETE FROM user_table;


EXPLAIN ANALYZE SELECT * FROM user_table WHERE name LIKE 'Name 500%';

EXPLAIN ANALYZE SELECT * FROM user_table WHERE name = 'Name 500';

EXPLAIN ANALYZE SELECT * FROM user_table WHERE email = 'email500@example.com';

