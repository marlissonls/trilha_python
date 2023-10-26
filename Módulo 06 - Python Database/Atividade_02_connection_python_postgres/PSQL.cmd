# psql -U postgres
    "OUTPUT"
    """"""
    psql (15.2 (Debian 15.2-1.pgdg110+1))
    Type "help" for help.
    """"""

postgres=# CREATE DATABASE pypostgres;
    "OUTPUT"
    """"""
    CREATE DATABASE
    """"""

postgres=# \l
    "OUTPUT"
    """"""
                                                    List of databases
        Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
    ------------+----------+----------+------------+------------+------------+-----------------+-----------------------
    db_python  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
    postgres   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
    pypostgres | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
    template0  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
                |          |          |            |            |            |                 | postgres=CTc/postgres
    template1  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
                |          |          |            |            |            |                 | postgres=CTc/postgres
    (5 rows)
    """"""

postgres=# \c pypostgres 
    "OUTPUT"
    """"""
    You are now connected to database "pypostgres" as user "postgres".
    """"""

pypostgres=# \dt
    "OUTPUT"
    """"""
            List of relations
    Schema |   Name   | Type  |  Owner   
    --------+----------+-------+----------
    public | register | table | postgres
    (1 row)
    """"""
