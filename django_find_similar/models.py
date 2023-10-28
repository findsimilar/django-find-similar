"""
django-find-similar main models
"""
from django.db import models


class Text(models.Model):
    """
    Simple unique text model
    """
    text = models.TextField(unique=True)


class FindSimilarInput(models.Model):
    """
    find-similar input params
    """
    # 'text': 'one two',
    text = models.ForeignKey(
                             Text,
                             on_delete=models.CASCADE,
                             related_name='text_find_similar_inputs'
                             )
    # 'texts': ['one', 'two'],
    texts = models.ManyToManyField(Text)
    # 'language': "english",
    language = models.CharField(max_length=128, default='english')
    # 'count': 5,
    count = models.PositiveIntegerField(default=5)
    # 'dictionary': None,
    # 'remove_stopwords': True,
    remove_stopwords = models.BooleanField(default=True)
    # 'keywords': None,
