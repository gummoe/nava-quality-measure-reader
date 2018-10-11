
class RecordItem:

    def __init__(self, value, schema_field):
        self.value = value
        self.schema_field = schema_field

    def get_schema_formatted_value(self):
        return self.schema_field.format_value_for_type(self.value)
