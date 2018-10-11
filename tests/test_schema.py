import unittest

from domain.schema import Schema
from domain.schema_field import SchemaField


class SchemaTest(unittest.TestCase):

    def test_init(self):
        schema = Schema()

        self.assertEqual([], schema.schema_fields)

    def test_add_schema_field(self):
        schema_field = SchemaField('', 1, '')
        schema = Schema()
        schema.add_schema_field(schema_field)
        schema.add_schema_field(schema_field)

        self.assertEqual(2, len(schema.schema_fields))
