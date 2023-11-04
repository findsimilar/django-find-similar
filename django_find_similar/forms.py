"""
Forms
"""
from django import forms


class FindSimilarForm(forms.Form):
    """
    Form to find find_similar
    """
    text = forms.CharField()
    language = forms.CharField(max_length=128, initial='english')
    remove_stopwords = forms.BooleanField(initial=True)

    class Meta:
        """
        Meta
        """
        fields = '__all__'
