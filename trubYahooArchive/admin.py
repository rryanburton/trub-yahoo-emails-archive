from django.contrib import admin
from django.contrib.admin import ModelAdmin

from trubYahooArchive.models import TrubEmail


class TrubEmailadmin(ModelAdmin):
    list_display = ('id',
                    'authorName',
                    'sender',
                    'subject',
                    'postDate',
                    'msgId',
                    'topicId',
                    'msgSnippet',
                    # 'rawEmail',
                    )


admin.site.register(TrubEmail, TrubEmailadmin)
