#!/usr/bin/env python3

import sys
import json
import jsonschema2db

src = sys.argv[1] if len(sys.argv) > 1 else 'tt.json'
schm = sys.argv[2] if len(sys.argv) > 2 else None
schema = json.load(open(src))
translator = jsonschema2db.JSONSchemaToPostgres(
    schema,
    postgres_schema = schm
)
print('=================== DDL =================')
translator.create_tables()
