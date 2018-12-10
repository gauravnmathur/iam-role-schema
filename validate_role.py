import os
import sys
import json
import jsonschema

def validate(schema_file, json_file):
    resolver = jsonschema.RefResolver('file://%s/' % os.path.abspath(os.path.dirname(__file__)), None)
    with open(schema_file, 'r') as fP:
        schema_schema = json.loads(fP.read())

    with open(json_file, 'r') as fP:
        json_data = json.loads(fP.read())

    try:
        jsonschema.validate(json_data, schema_schema, resolver=resolver)
    except jsonschema.exceptions.ValidationError as ve:
        print str(ve)


if __name__ == "__main__":
    validate(sys.argv[1], sys.argv[2])

