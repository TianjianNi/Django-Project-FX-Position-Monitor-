from django.db import models

# Create your models here.
CURRENCY_CHOICES = [
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('EUR', 'Euro'),
    ('JPY', 'Japanese Yen'),
    ('NZD', 'New Zealand Dollar'),
    ('NOK', 'Norwegian Krone'),
    ('GBP', 'Pound Sterling'),
    ('SEK', 'Swedish Krona'),
    ('CHF', 'Swiss Franc'),
    ('USD', 'United States Dollar'),
]

BUY_SELL_CHOICES = [
    ('BUY', 'buy'),
    ('SELL', 'sell'),
]

class Trade(models.Model):
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='AUD')
    buy_sell = models.CharField(max_length=4, choices=BUY_SELL_CHOICES, default='BUY')
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.buy_sell + ' ' + self.currency + ' amount: ' + str(self.amount)