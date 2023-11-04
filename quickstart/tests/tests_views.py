"""
Tests for views
"""
from django.urls import reverse
from dry_tests import SimpleTestCase, TestCase, Request, TrueResponse, Context, POST

from django_find_similar.forms import FindSimilarForm
from django_find_similar.models import TextToken, CheckResult


def url():
    """
    url for find fimilar
    """
    return reverse('quickstart:find_similar')


def results_url():
    """
    url for result list
    """
    return reverse('quickstart:results')


class FindSimilarFormViewSimpleTestCase(SimpleTestCase):
    """
    Test for FindSimilarForm view
    """
    def test_get(self):
        """
        Test get request
        """
        request = Request(
            url=url(),
        )

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['form'],
                types={
                    'form': FindSimilarForm,
                }
            ),
            content_values=[
                'form'
            ]
        )

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class FindSimilarFormViewTestCase(TestCase):
    """
    Test form view
    """

    def test_post(self):
        """
        Test post requests
        """
        data = {
            'text': 'one two',
            'language': 'english',
            'remove_stopwords': True,
        }

        request = Request(
            method=POST,
            url=url(),
            data=data,
        )

        true_response = TrueResponse(
            status_code=302,
            redirect_url=results_url(),
        )

        # db state before
        text_tokens = [
            TextToken(
                text='one',
            ),
            TextToken(
                text='two',
            ),
        ]
        TextToken.objects.bulk_create(text_tokens)

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

        # db state after (result needed)
        # result has been saved
        self.assertEqual(CheckResult.objects.count(), 1)


class TestResultListView(TestCase):
    """
    Tests for results list
    """
    def setUp(self):
        self.url = results_url()

    def test_get(self):
        """
        Test get request
        """
        request = Request(
            url = self.url,
        )

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['object_list'],
            ),
        )

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)
