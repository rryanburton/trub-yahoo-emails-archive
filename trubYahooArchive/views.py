import json
import os

from django.shortcuts import render
from django.views.generic import ListView

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
                rawmsg = data.get('rawEmail')
                print(type(rawmsg))
                splitlines = rawmsg.splitlines()
                print("data loaded: {}, starting serializer".format(splitlines))

                # for thing in data:
                count += 1

                serializer = EmailSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    successful += 1
                    print("ok {}".format(successful))
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
