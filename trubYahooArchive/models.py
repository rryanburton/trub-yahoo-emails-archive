from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime


class TrubEmail(models.Model):
    authorName = models.CharField(max_length=250, blank=True, null=True)
    sender = models.CharField(max_length=250)
    subject = models.CharField(max_length=250, blank=True, null=True)
    postDate = models.DateTimeField(blank=True, null=True)
    msgId = models.IntegerField(blank=True, null=True)
    topicId = models.IntegerField(blank=True, null=True)
    msgSnippet = models.TextField(blank=True, null=True)
    rawEmail = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('email-detail', args=[str(self.id)])

    def date(self):
        # return datetime(int(self.postDate)).date()

        return datetime.fromtimestamp(int(self.postDate)).strftime('%c')
