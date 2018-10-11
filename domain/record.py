
class Record:

    def __init__(self):
        self.record_items = []

    def add_record_item(self, record_item):
        self.record_items.append(record_item)

    def to_dict(self):
        dict = {}
        for record_item in self.record_items:
            dict[record_item.schema_field.field_name] = record_item.get_schema_formatted_value()
        return dict
