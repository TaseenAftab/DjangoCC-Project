from django.db import models
from django.urls import reverse

class Ifta(models.Model):

    class FiqhChoices(models.TextChoices):
        HANAFI = "hanafi", "Hanafi"
        MALIKI = "maliki", "Maliki"
        SHAFI = "shafi", "Shafi'"
        HANBALI = "hanbali", "Hanbali"

    name = models.CharField(max_length=100)
    fiqh = models.CharField(
        max_length=20,
        choices=FiqhChoices.choices,
        null=False,
        blank=False,
    )
    

    def __str__(self):
        return f'{self.name.capitalize()} : ({self.fiqh.capitalize()})'
    
    def get_absolute_url(self):
        return reverse('testapp:ifta_detail', args=[self.name])
