from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from sortable_listview import SortableListView

from trubYahooArchive.models import TrubEmail


class EmailList(ListView):
    model = TrubEmail
    ordering = 'postDate'
    paginate_by = 20


class SortableEmailList(SortableListView):
    allowed_sort_fields = {'sender': {'default_direction': '',
                                      'verbose_name': 'Sender'},
                           'postDate': {'default_direction': '',
                                        'verbose_name': 'Date'},

                           }
    default_sort_field = 'postDate'
    paginate_by = 20
    template_name = 'trubYahooArchive/trubemail_list.html'
    model = TrubEmail


class EmailSearchList(ListView):
    model = TrubEmail
    ordering = 'postDate'
    paginate_by = 20
    template_name = 'trubYahooArchive/trub_search_email_list.html'


class EmailSearchResultsView(ListView):
    model = TrubEmail
    template_name = 'trubYahooArchive/trub_search_email_list.html'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = TrubEmail.objects.filter(
            Q(rawEmail__icontains=query) | Q(sender__icontains=query)
        )
        return object_list


class EmailDetail(DetailView):
    model = TrubEmail

    def splitlines(self):
        obj = self.get_object()
        splitlines = obj.rawEmail.splitlines()
        return splitlines


class IndexView(TemplateView):
    template_name = 'trubYahooArchive/index.html'
