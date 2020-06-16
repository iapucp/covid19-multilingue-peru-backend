from core.models import Language
from django.test import SimpleTestCase


class LanguageTestCase(SimpleTestCase):
    """
    SimpleTestCase is used to avoid default Django database connection.

    setUp and tearDown methods include some basic table rename to separate from
    dev environment
    """

    def setUp(self):
        Language.Meta.table_name = "test_" + Language.Meta.table_name
        Language.create_table()
        Language('AC', name='ACHUAR').save()
        Language('QU', name='QUECHUA').save()

    def test_query_language(self):
        """
        Just a sample test c:
        """
        language = Language.get('AC')
        self.assertEqual(language.name, 'ACHUAR')

    def tearDown(self):
        Language.delete_table()
