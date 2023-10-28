"""
Tests for models
"""
from django.test import TestCase
# from find_similar import find_similar
from django_find_similar.models import FindSimilarInput, Text


class FindSimilarInputTestCase(TestCase):
    """
    Test FindSimilarInput model
    """

    def test_create(self):
        """
        Test properties
        """
        input_data = {
            'text': Text.objects.create(text='one two'),
            # 'texts': [Text.objects.create(text='one'), Text.objects.create(text='two')],
            'language': "english",
            'count': 5,
            # 'dictionary': None,
            'remove_stopwords': True,
            # 'keywords': None,
        }
        find_similar_input = FindSimilarInput.objects.create(
            **input_data
        )

        texts = [Text.objects.create(text='one'), Text.objects.create(text='two')]

        for text in texts:
            find_similar_input.texts.add(text)
        find_similar_input.save()

        self.assertEqual(find_similar_input.text, input_data['text'])
