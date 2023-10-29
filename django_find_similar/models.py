"""
django-find-similar main models
"""
from django.db import models
from find_similar import find_similar, TokenText as FindSimilarTokenText
from find_similar.tokenize import tokenize


class AbstractTimestamp(models.Model):

    class Meta:
        abstract = True

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class AbstractTextToken(AbstractTimestamp):
    text = models.TextField()
    language = models.CharField(max_length=128, default='english')
    remove_stopwords = models.BooleanField(default=True)
    cos = models.FloatField(blank=True, null=True)

    def has_tokens(self):
        return self.token_set.all().exists()

    def create_tokens(self):
        token_set = tokenize(self.text, language=self.language, remove_stopwords=self.remove_stopwords)
        tokens = map(lambda text_str: Token(value=text_str, token_text=self), token_set)
        Token.objects.bulk_create(tokens)

    class Meta:
        abstract = True


class TextToken(AbstractTextToken):
    pass


class AbstractToken(AbstractTimestamp):

    class Meta:
        abstract = True

    value = models.TextField()
    token_text = models.ForeignKey(TextToken, on_delete=models.CASCADE)


class Token(AbstractToken):
    pass


def find_similar_models(text: AbstractTextToken, texts):
    return [text]