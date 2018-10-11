
class SchemaField:

    def __init__(self, field_name, field_length, field_type):
        self.field_name = field_name
        self.field_length = int(field_length)
        self.field_type = field_type

    def format_value_for_type(self, value):
        try:
            if self.field_type == 'INTEGER':
                return int(value)
            elif self.field_type == 'BOOLEAN':
                return int(value) > 0
            elif self.field_type == 'TEXT':
                return str(value)
            else:
                return value
        except ValueError:
            return value
