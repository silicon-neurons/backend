from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass # todo?

class Post(models.Model):
    PERSUASIVE = 'P'
    NUDGE = 'N'
    HOSTILE = 'H'
    DESIGN_TYPES = (
        (PERSUASIVE, 'Persuasive'),
        (NUDGE, 'Nudge'),
        (HOSTILE, 'Hostile'),
    )

    image = models.ImageField(upload_to='pics/%Y/%m/%d/')
    desc = models.TextField('Description', max_length=280)
    design = models.CharField(max_length=1, choices=DESIGN_TYPES)
    score = models.FloatField(default=1.0)
    geotag = models.CharField(max_length=56) # unsure
    timestamp = models.DateTimeField('Date Added', auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    lens = models.ForeignKey("Lens", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '{} on {}'.format(self.design, self.timestamp)

class Lens(models.Model):
    title = models.CharField(max_length=30)
    desc = models.CharField('Description', max_length=50)
    timestamp = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField('Description', max_length=50)
    timestamp = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return self.title

class Correction(models.Model):
    PERSUASIVE = 'P'
    NUDGE = 'N'
    HOSTILE = 'H'
    DESIGN_TYPES = (
        (PERSUASIVE, 'Persuasive'),
        (NUDGE, 'Nudge'),
        (HOSTILE, 'Hostile'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    agrees = models.BooleanField()
    replace = models.CharField('Suggested Correction', max_length=1, choices=DESIGN_TYPES)
    timestamp = models.DateTimeField('Date Added', auto_now_add=True)

    def __str__(self):
        return 'Agreed' if self.agrees else 'Disagreed'
