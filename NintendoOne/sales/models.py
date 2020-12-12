from django.db import models
from djmoney.models.fields import MoneyField
import urllib, os
from urllib.parse import urlparse

# Create your models here.

class Game(models.Model):
    '''
    Stores game information such as name, description, release date, image etc...
    '''
    name = models.CharField(max_length=40)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=200, default='')

    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/game/', null=True, blank=True)
    
    is_new = models.BooleanField(default=False)
    membership_required = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        '''
        before save to db, download the game image
        '''
        if self.image_url:
            file_save_dir = 'static/images/game/'
            filename = urlparse(self.image_url).path.split('/')[-1]
            urllib.request.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
            self.image = os.path.join(file_save_dir, filename)
            self.image_url = ''
        super(Game, self).save()

class GamePrice(models.Model):
    '''
    Stores game price information for each region.
    '''
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    on_sale = models.BooleanField(default=False)
    # this field is used to distinguish new discounts from the old ones
    _hash = models.CharField(max_length=40)

    currency = models.CharField(max_length=10)
    region = models.CharField(max_length=30) # stores country code
    regular_price = MoneyField(max_digits=14, decimal_places=2)
    discount_price = MoneyField(max_digits=14, decimal_places=2)

    discount_start = models.DateTimeField()
    discount_end = models.DateTimeField()


class GameScreenShot(models.Model):
    '''
    Stores game screenshots provided by Nintendo official API
    '''
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='static/images/game/screenshots')
    image_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        '''
        before save to db, download the game image
        '''
        if self.image_url:
            file_save_dir = 'static/images/game/screenshots'
            filename = urlparse(self.image_url).path.split('/')[-1]
            urllib.request.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
            self.image = os.path.join(file_save_dir, filename)
            self.image_url = ''
        super(Game, self).save()
