"""
Forms
"""
from django import forms


class FindSimilarParamsForm(forms.Form):
    """
    Form with find-similar params
    """
    language = forms.CharField(max_length=128, initial='english')
    remove_stopwords = forms.BooleanField(initial=True)


class FindSimilarForm(FindSimilarParamsForm):
    """
    Form to find find_similar
    """
    text = forms.CharField()
