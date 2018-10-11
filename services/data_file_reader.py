from domain.record import Record
from domain.record_item import RecordItem


class DataFileReader:

    @classmethod
    def parse_data_with_schema(cls, file, schema):
        records = []
        for line in file:
            record = Record()
            line_list = [char for char in line]

            for schema_field in schema.schema_fields:
                value = ''.join(line_list[0:schema_field.field_length])
                record_item = RecordItem(value, schema_field)
                record.add_record_item(record_item)
                del line_list[0:schema_field.field_length]

            records.append(record)

        file.close()
        return records
