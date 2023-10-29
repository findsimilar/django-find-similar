from django.test import TestCase
from django_find_similar.models import TextToken
from django_find_similar.adapter import TokenTextAdapter
from find_similar import TokenText, find_similar


class AdapterTestCase(TestCase):

    def setUp(self):
        self.text_str = 'one two'
        self.text_token = TextToken.objects.create(text=self.text_str)
        self.token_text: TokenText = TokenTextAdapter(self.text_token)

    def test_adapter(self):
        self.assertTrue(isinstance(self.token_text, TokenText))
        self.assertEqual(self.token_text.text, self.text_str)

    def test_find_similar(self):
        result = find_similar(self.token_text, [self.token_text])
        self.assertEqual(len(result), 1)
        first = result[0]
        self.assertEqual(first.cos, 1.0)
        self.assertIsNone(first.text_token_model.cos)
        first.save_cos()
        self.assertEqual(first.text_token_model.cos, 1.0)
