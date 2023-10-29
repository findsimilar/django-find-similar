"""
Tests for models
"""
from django.test import TestCase
from find_similar import find_similar, TokenText
from django_find_similar.models import TextToken, Token, find_similar_models


class ModelsTestCase(TestCase):

    def setUp(self):
        self.text_str = 'one two'
        self.text_token = TextToken.objects.create(text=self.text_str)

    def test_text_to_token_text(self):
        self.assertEqual(self.text_token.text, self.text_str)
        self.assertEqual(self.text_token.language, 'english')
        self.assertTrue(self.text_token.remove_stopwords)

    def test_create_tokens(self):
        self.assertFalse(self.text_token.has_tokens())
        self.text_token.create_tokens()
        self.assertTrue(self.text_token.has_tokens())
        self.assertEqual(self.text_token.token_set.count(), 2)
        tokens_str = ['one', 'two']
        for token_str in tokens_str:
            self.assertTrue(self.text_token.token_set.filter(value=token_str).exists())
