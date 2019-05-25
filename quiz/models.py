from django.db import models


# Create your models here.

class Quiz(models.Model):
    pr_id = models.IntegerField(primary_key=True, unique=True, blank=False)
    subject = models.CharField(max_length=50, blank=False)
    image = models.URLField(blank=True)
    title = models.TextField()
    answer = models.IntegerField()
    explain = models.TextField()
    choice_1 = models.CharField(max_length=50)
    choice_2 = models.CharField(max_length=50)
    choice_3 = models.CharField(max_length=50)
    choice_4 = models.CharField(max_length=50)

    class Meta:
        ordering = ('subject',)



