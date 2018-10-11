import csv

from domain.schema_field import SchemaField
from domain.schema import Schema


class SchemaFileReader:

    @classmethod
    def convert_file_to_schema(cls, file):
        schema = Schema()
        csv_file_reader = csv.reader(file, delimiter=' ')
        for row in csv_file_reader:
            fields = row[0].split(',')
            field_name = fields[0]
            field_length = fields[1]
            field_type = fields[2]
            schema_field = SchemaField(field_name, field_length, field_type)
            schema.add_schema_field(schema_field)

        file.close()
        return schema
