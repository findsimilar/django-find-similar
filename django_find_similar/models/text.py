"""
django-find-similar main models
"""
from django.db import models
from find_similar.tokenize import tokenize


class AbstractTimestamp(models.Model):
    """
    create and update benchmarks
    """

    class Meta:
        """
        Meta
        """
        abstract = True

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class AbstractTextToken(AbstractTimestamp):
    """
    Abstract class for TextToken
    """

    text = models.TextField()
    language = models.CharField(
        max_length=128,
        default='english'
    )
    remove_stopwords = models.BooleanField(default=True)
    cos = models.FloatField(blank=True, null=True)

    def has_tokens(self):
        """
        Has tokens
        """
        return self.token_set.all().exists()

    def create_tokens(self):
        """
        Create tokens
        """
        token_set = tokenize(
            self.text,
            language=self.language,
            remove_stopwords=self.remove_stopwords
        )
        tokens = map(lambda text_str: Token(value=text_str, token_text=self), token_set)
        Token.objects.bulk_create(tokens)

    class Meta:
        """
        Meta
        """
        abstract = True
        unique_together = ["text", "language", "remove_stopwords"]


class TextToken(AbstractTextToken):
    """
    TextoToken
    """


class AbstractToken(AbstractTimestamp):
    """
    Abstract class for Token
    """

    class Meta:
        """
        Meta
        """
        abstract = True
        unique_together = ["value", "token_text"]

    value = models.TextField()
    token_text = models.ForeignKey(TextToken, on_delete=models.CASCADE)


class Token(AbstractToken):
    """
    Token
    """
