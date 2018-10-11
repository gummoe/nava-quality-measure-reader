import os
import sys

from services.schema_file_reader import SchemaFileReader
from services.data_file_reader import DataFileReader
from services.api_client import APIClient

SCHEMAS_FILE_PATH = '/schemas/'
SCHEMAS_FILE_TYPE = '.csv'
DATA_FILE_PATH = '/data/'
DATA_FILE_TYPE = '.txt'


def main():
    args = sys.argv

    filename = args[1]
    schema_file = get_file(filename, SCHEMAS_FILE_PATH, SCHEMAS_FILE_TYPE)
    data_file = get_file(filename, DATA_FILE_PATH, DATA_FILE_TYPE)
    schema = SchemaFileReader.convert_file_to_schema(schema_file)
    records = DataFileReader.parse_data_with_schema(data_file, schema)

    for record in records:
        APIClient.post_measures_record(record)


def get_file(filename, directory, file_type):
    file_path = os.path.dirname(os.path.abspath(__file__)) + directory + filename + file_type
    file = open(file_path)
    return file


if __name__ == '__main__':
    main()
