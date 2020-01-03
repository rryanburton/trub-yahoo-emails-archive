import json
import os
from html import unescape

from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.utils.html import escape
from django.views.generic import ListView, DetailView

from trubYahooArchive.models import TrubEmail
from trubYahooArchive.serializers import EmailSerializer


def parse_json(request):
    successful = 0
    fails = 0
    count = 0
    fail_list = ""
    for filename in os.listdir('./data/'):
        if filename.endswith('.json'):
            with open(os.path.join('./data/', filename)) as json_data:
                data = json.load(json_data)
                # successful = 0
                # fails = 0
                # count = 0
                # fail_list = ""
                data = data.get('ygData')
                data['sender'] = unescape(data.pop('from'))
                data['postDate'] = datetime.fromtimestamp(int(data.pop('postDate')))
                # data['']
                rawmsg = data.get('rawEmail')
                splitlines = rawmsg.splitlines()
                # for item in splitlines:
                #     print(unescape(item))

                # print("data loaded: {}, starting serializer".format(splitlines))

                # for thing in data:
                count += 1

                serializer = EmailSerializer(data=data)
                # print("fields: {}".format(serializer))
                if serializer.is_valid():
                    serializer.save()
                    successful += 1
                    # print("ok {}".format(successful))
                else:
                    print("serializer was not valid")
                    # print(person)
                    # print(serializer.errors)
                    fail_list += repr(serializer.errors) + ","
                    fails += 1

    print(
        "all done with process. ok: {}. fails: {}. Out of {} total records".format(
            successful, fails, count))
    if fail_list != "":
        print("fails: {}".format(fail_list))
    return render(request, 'trubYahooArchive/index.html',
                  {'successful': successful,
                   'fails': fails,
                   'count': count,
                   'data': splitlines,
                   },
                  )


class EmailList(ListView):
    model = TrubEmail
    ordering = 'postDate'


class EmailDetail(DetailView):
    model = TrubEmail

    def splitlines(self):
        obj = self.get_object()
        splitlines = obj.rawEmail.splitlines()
        return splitlines

