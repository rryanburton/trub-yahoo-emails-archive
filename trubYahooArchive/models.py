from django.db import models


class TrubEmail(models.Model):
    authorName = models.CharField(max_length=250, blank=True, null=True)
    sender = models.CharField(max_length=250, blank=True, null=True)
    replyTo = models.CharField(max_length=250, blank=True, null=True)

    subject = models.CharField(max_length=250, blank=True, null=True)
    postDate = models.CharField(max_length=250, blank=True, null=True)
    msgId = models.IntegerField(blank=True, null=True)

    topicId = models.IntegerField(blank=True, null=True)
    msgSnippet = models.TextField(blank=True, null=True)
    rawEmail = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return str(self.pk)
