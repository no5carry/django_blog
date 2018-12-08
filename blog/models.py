from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    nickname = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    PODCAST = 'PC'
    LIFE = 'LF'
    CYBERWOLD = 'CW'
    THEM_CHOICES = (
        (PODCAST, 'Podcast'),
        (LIFE, 'Life'),
        (CYBERWOLD, 'CyberWorld'),
    )
    them = models.CharField(
        max_length=2,
        choices=THEM_CHOICES,
        default=CYBERWOLD,
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish():
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
