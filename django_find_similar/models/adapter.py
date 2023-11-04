"""
Adapters for find_similar
"""
from find_similar import TokenText
from .text import AbstractTextToken, Token


class TokenTextAdapter(TokenText):
    """
    Adapter to find_similar TokenText
    """

    def __init__(self, text_token_model: AbstractTextToken):
        self.text_token_model = text_token_model
        if not self.text_token_model.has_tokens():
            self.text_token_model.create_tokens()

        super().__init__(
            text=self.text_token_model.text,
            tokens=None,
            dictionary=None,
            language=self.text_token_model.language,
            remove_stopwords=self.text_token_model.remove_stopwords,
        )


        # save tokens to db
        Token.objects.filter(token_text=self.text_token_model).delete()
        tokens = map(
            lambda text_str: Token(value=text_str, token_text=self.text_token_model),
            self.tokens
        )
        Token.objects.bulk_create(tokens)

    def save_cos(self):
        """
        save cos to text token
        """
        if self.cos:
            self.text_token_model.cos = self.cos
            self.text_token_model.save()
