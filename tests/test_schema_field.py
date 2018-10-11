import unittest

from domain.schema_field import SchemaField


class SchemaFieldTest(unittest.TestCase):

    def test_init(self):
        field_name = 'bananas'
        field_length = 32
        field_type = 'TEXT'
        schema_field = SchemaField(field_name, field_length, field_type)

        self.assertEqual(field_name, schema_field.field_name)
        self.assertEqual(field_length, schema_field.field_length)
        self.assertEqual(field_type, schema_field.field_type)

    def test_format_value_for_type_integer(self):
        schema_field = SchemaField('coffee', 200, 'INTEGER')
        string_test_input = '5'
        num_test_input = 5
        bad_test_input = 'juniper'

        self.assertEqual(5, schema_field.format_value_for_type(string_test_input))
        self.assertEqual(5, schema_field.format_value_for_type(num_test_input))
        self.assertEqual(bad_test_input, schema_field.format_value_for_type(bad_test_input))

    def test_format_value_for_type_boolean(self):
        schema_field = SchemaField('coffee', 200, 'BOOLEAN')
        string_test_input = '1'
        num_test_input = 1
        bad_test_input = 'marshmellow'

        self.assertTrue(schema_field.format_value_for_type(string_test_input))
        self.assertTrue(schema_field.format_value_for_type(num_test_input))
        self.assertEqual(bad_test_input, schema_field.format_value_for_type(bad_test_input))

    def test_format_value_for_type_text(self):
        schema_field = SchemaField('coffee', 200, 'TEXT')
        string_test_input = '100'
        num_test_input = 52

        self.assertEqual('100', schema_field.format_value_for_type(string_test_input))
        self.assertTrue('52', schema_field.format_value_for_type(num_test_input))

