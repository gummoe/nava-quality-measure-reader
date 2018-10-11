import unittest

from domain.record_item import RecordItem
from domain.schema_field import SchemaField


class RecordItemTest(unittest.TestCase):

    def test_init(self):
        value = 18
        schema_field = SchemaField('name', 0, 'TEXT')
        record_item = RecordItem(value, schema_field)

        self.assertEqual(value, record_item.value)
        self.assertEqual(schema_field, record_item.schema_field)
