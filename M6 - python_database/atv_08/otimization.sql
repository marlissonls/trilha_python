CREATE TABLE user_table (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);



CREATE INDEX name_index ON user_table (name);



-- Populando com 1 mil registros
INSERT INTO user_table (name, email)
SELECT 
  'Name ' || generate_series(1, 1000),
  'email' || generate_series(1, 1000) || '@example.com'
FROM generate_series(1, 1000);

-- Populando com 10 mil registros
INSERT INTO user_table (name, email)
SELECT 
  'Name ' || generate_series(1, 10000),
  'email' || generate_series(1, 10000) || '@example.com'
FROM generate_series(1, 10000);

-- Populando com 100 mil registros
INSERT INTO user_table (name, email)
SELECT 
  'Name ' || generate_series(1, 100000),
  'email' || generate_series(1, 100000) || '@example.com'
FROM generate_series(1, 100000);

-- Populando com 1 milhão de registros
INSERT INTO user_table (name, email)
SELECT 
  'Name ' || generate_series(1, 1000000),
  'email' || generate_series(1, 1000000) || '@example.com'
FROM generate_series(1, 1000000);

DELETE FROM user_table;



EXPLAIN ANALYZE SELECT * FROM user_table WHERE name LIKE 'Name 500%';

EXPLAIN ANALYZE SELECT * FROM user_table WHERE name = 'Name 500';

EXPLAIN ANALYZE SELECT * FROM user_table WHERE email = 'email500@example.com';


CREATE TABLE comparacao_resultados (
  requisicao VARCHAR(1),
  quantidade_dados VARCHAR(10),
  tempo_execucao DOUBLE PRECISION
);
