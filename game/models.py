from django.db import models

# Create your models here.
class Game(models.Model):
    title =  models.CharField(max_length=100, null=False, verbose_name='Game Title')

    def __unicode__(self):
        return self.name