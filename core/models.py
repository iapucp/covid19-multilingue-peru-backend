from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class Language(Model):

    class Meta:
        table_name = "core_languages"
        host = "http://db:8000"
        read_capacity_units = 4
        write_capacity_units = 4

    code = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
