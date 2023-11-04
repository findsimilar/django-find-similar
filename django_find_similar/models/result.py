"""
Result models
"""
from django.db import models
from .text import AbstractTimestamp, TextToken
from .adapter import TokenTextAdapter


class CheckResult(AbstractTimestamp):
    """
    Result class
    """
    text = models.ForeignKey(TextToken, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)

    @classmethod
    def save_result(cls, text: TextToken, result: list):
        """
        Save find_similar result
        """
        check_result = cls.objects.create(text=text)
        # save items
        for order, item in enumerate(result):
            CheckResultItem.save_result(item, order, check_result)
        return check_result


class CheckResultItem(AbstractTimestamp):
    """
    One result item
    """
    text = models.ForeignKey(TextToken, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    cos = models.FloatField(default=0.0)
    result = models.ForeignKey(CheckResult, on_delete=models.CASCADE)

    @classmethod
    def save_result(cls, item: TokenTextAdapter, order: int, check_result: CheckResult):
        """
        Save find_similar result
        """
        text_token = item.text_token_model
        check_result_item = CheckResultItem.objects.create(
            text=text_token,
            order=order,
            cos=item.cos,
            result=check_result,
        )
        return check_result_item

    def cos_percent(self):
        """
        Get cos percent
        """
        return round(self.cos * 100)
