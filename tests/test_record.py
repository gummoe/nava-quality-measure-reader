import unittest

from domain.record import Record
from domain.record_item import RecordItem
from domain.schema_field import SchemaField


class RecordTest(unittest.TestCase):

    def test_init(self):
        record = Record()

        self.assertEqual([], record.record_items)

    def test_add_record_item(self):
        schema_field = SchemaField('', 0, 'TEXT')
        record_item = RecordItem(1, schema_field)
        record = Record()
        record.add_record_item(record_item)
        record.add_record_item(record_item)

        self.assertEqual(2, len(record.record_items))

    def test_to_dict(self):
        record = Record()

        schema_field_text = SchemaField('field1', 10, 'TEXT')
        record_item_text = RecordItem('hello', schema_field_text)
        record.add_record_item(record_item_text)

        schema_field_int = SchemaField('field2', 11, 'INTEGER')
        record_item_int = RecordItem(18, schema_field_int)
        record.add_record_item(record_item_int)

        schema_field_bool = SchemaField('field3', 1, 'BOOLEAN')
        record_item_bool = RecordItem(0, schema_field_bool)
        record.add_record_item(record_item_bool)

        expected_output = {
            'field1': 'hello',
            'field2': 18,
            'field3': False
        }

        self.assertEqual(expected_output, record.to_dict())




