from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    email = models.EmailField('Email', max_length=160, unique=True)
    telegram_id = models.CharField('Telegram Id', max_length=50, unique=True)
    notify_to_telegram = models.BooleanField('Send notificaitons to Telegram', default=True)
    notify_to_email = models.BooleanField('Send notifications to email', default=False)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('pro', 'Pro'),
    ]
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    member_since = models.DateField('Member since', auto_now_add=True)
    is_active = models.BooleanField('Active', default=True)
    membership_type = models.CharField('Membership type', max_length=25, choices=MEMBERSHIP_TYPES)
    valid_thru = models.DateField('Valid thru', null=True, blank=True)

    def __str__(self):
        return f'{self.user} - Membership type: {self.membership_type} - Member since: {self.member_since}'


class Exchange(models.Model):
    EXCHANGE_LIST = [
        ('binance', 'Binance'),
        ('buda', 'Buda'),
        ('gemini', 'Gemini'),
        ('bitso', 'Bitso'),
        ('okcoin', 'OKCoin'),
        ('bitstamp1', 'Bitstamp'),
    ]
    name =  models.CharField('CCXT exchange id', max_length=100, choices=EXCHANGE_LIST)

    def __str__(self):
        return self.name


class UserExchange(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    exchange = models.ForeignKey(Exchange, on_delete=models.RESTRICT)
    api_key = models.CharField('API Key', max_length=100)
    api_secret = models.CharField('API Secret', max_length=100)

    def __str__(self):
        return f'User: {self.user.first_name}, Exchange: {self.exchange.name}'