import json
import os
from html import unescape

from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.utils.html import escape
from django.views.generic import ListView, DetailView, TemplateView

from trubYahooArchive.models import TrubEmail
from trubYahooArchive.serializers import EmailSerializer


def parse_json(request):
    successful = 0
    fails = 0
    skips = 0
    count = 0
    fail_list = ""
    datadir = './data/'
    for filename in os.listdir(datadir):
        if filename.endswith('.json'):
            with open(os.path.join(datadir, filename)) as json_data:
                data = json.load(json_data)
                # successful = 0
                # fails = 0
                # count = 0
                # fail_list = ""

                data = data.get('ygData')
                msgId = data['msgId']
                data['sender'] = unescape(data.pop('from'))
                try:
                    data['postDate'] = datetime.fromtimestamp(int(data.pop('postDate')))
                except:
                    print("{} no postDate".format(msgId))
                    continue
                # data['']

                # print(msgId)
                rawmsg = data.get('rawEmail')
                splitlines = rawmsg.splitlines()
                # for item in splitlines:
                #     print(unescape(item))

                # print("data loaded: {}, starting serializer".format(splitlines))

                # for thing in data:
                count += 1
                if not TrubEmail.objects.get(msgId__exact=msgId):
                    serializer = EmailSerializer(data=data)

                    # print("fields: {}".format(serializer))
                    if serializer.is_valid():
                        serializer.save()
                        successful += 1
                        print("ok {}".format(msgId))
                    else:
                        print("{} serializer was not valid".format(msgId))
                        # print(person)
                        # print(serializer.errors)
                        fail_list += repr(serializer.errors) + ","
                        fails += 1
                else:
                    skips += 1

    print(
        "all done with process. ok: {}. fails: {}. Out of {} total records".format(
            successful, fails, count))
    if fail_list != "":
        print("fails: {}".format(fail_list))
    return render(request, 'trubYahooArchive/importjson.html',
                  {'successful': successful,
                   'fails': fails,
                   'count': count,
                   'skips': skips,
                   'data': splitlines,
                   },
                  )


class EmailList(ListView):
    model = TrubEmail
    ordering = 'postDate'
    paginate_by = 10


class EmailDetail(DetailView):
    model = TrubEmail

    def splitlines(self):
        obj = self.get_object()
        splitlines = obj.rawEmail.splitlines()
        return splitlines


class IndexView(TemplateView):
    template_name = 'trubYahooArchive/index.html'
