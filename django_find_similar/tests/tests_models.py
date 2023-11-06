"""
Tests for models
"""
from django.db.utils import IntegrityError
from django.test import TestCase
from find_similar import TokenText, find_similar
from django_find_similar.models import TextToken, CheckResult, CheckResultItem, TokenTextAdapter


class ModelsTestCase(TestCase):
    """
    Test for models
    """

    def setUp(self):
        """
        Set up test data
        """
        self.text_str = 'one two'
        self.text_token = TextToken.objects.create(text=self.text_str)

    def test_unique(self):
        """save the save text token"""
        with self.assertRaises(IntegrityError):
            TextToken.objects.create(
                text=self.text_token.text,
                language=self.text_token.language,
                remove_stopwords=self.text_token.remove_stopwords
            )

    def test_text_to_token_text(self):
        """
        test save
        """
        self.assertEqual(self.text_token.text, self.text_str)
        self.assertEqual(self.text_token.language, 'english')
        self.assertTrue(self.text_token.remove_stopwords)

    def test_create_tokens(self):
        """
        test create tokens
        """
        self.assertFalse(self.text_token.has_tokens())
        self.text_token.create_tokens()
        self.assertTrue(self.text_token.has_tokens())
        self.assertEqual(self.text_token.token_set.count(), 2)
        tokens_str = ['one', 'two']
        for token_str in tokens_str:
            self.assertTrue(self.text_token.token_set.filter(value=token_str).exists())


class TestCheckResult(TestCase):
    """
    Test check result
    """

    def setUp(self):
        self.text_str = 'one two'
        self.text_token = TextToken.objects.create(text=self.text_str)

    def test_save_result(self):
        """
        Test save_result
        """
        self.token_text: TokenText = TokenTextAdapter(self.text_token)
        result = find_similar(self.token_text, [self.token_text])

        # db before
        self.assertFalse(CheckResult.objects.all().exists())
        self.assertFalse(CheckResultItem.objects.all().exists())

        check_result = CheckResult.save_result(self.token_text.text_token_model, result)

        # db before
        # return result object
        self.assertEqual(check_result.text.id, self.text_token.id)
        self.assertEqual(check_result.checkresultitem_set.count(), 1)

    def test_str(self):
        """
        Test str method
        """
        check_result = CheckResult.objects.create(text=self.text_token)
        expected_str = str(self.text_token)
        self.assertEqual(str(check_result), expected_str)


class TestTextToken(TestCase):
    """
    Test TextToken
    """

    def test_get_token_set(self):
        """
        Test get_token_set
        """
        text_token = TextToken.objects.create(text='one two')
        self.assertEqual(text_token.get_token_set(), set())
        text_token.create_tokens()
        self.assertEqual(text_token.get_token_set(), {'one', 'two'})
