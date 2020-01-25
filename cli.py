#!/usr/local/bin/python3

import json
import jsonschema2db
import psycopg2

schema = json.load(open('all.json'))
translator = jsonschema2db.JSONSchemaToPostgres(
    schema,
    postgres_schema='tt'
)
print(translator)
con = psycopg2.connect('host=127.0.0.1 user=postgres dbname=zhu')
translator.create_tables(con)
