"""
Test for forms
"""
from django import forms
from dry_tests import SimpleTestCase
from dry_tests.models import TrueForm, Fields
from django_find_similar.forms import FindSimilarForm


class FindSimilarFormSimpleTestCase(SimpleTestCase):
    """
    Form page test
    """

    def test_form(self):
        """
        test form fields
        """
        current_form = FindSimilarForm()
        true_form = TrueForm(
            Fields(
                types={
                    'text': forms.CharField,
                    'language': forms.CharField,
                    'remove_stopwords': forms.BooleanField,
                }
            )
        )
        self.assertTrueForm(current_form, true_form)

    def test_form_valid(self):
        """
        Test valid and invalid form
        """
        form = FindSimilarForm(
            data={
                'text': 'one two'
            }
        )
        self.assertFalse(form.is_valid())

        form = FindSimilarForm(
            data={
                'text': 'one two',
                'language': 'english',
                'remove_stopwords': True,
            }
        )
        self.assertTrue(form.is_valid())
