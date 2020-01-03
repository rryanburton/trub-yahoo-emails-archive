from collections import OrderedDict

from rest_framework import serializers, viewsets

from .models import (
    TrubEmail,
)

#
class EmailSerializer(serializers.ModelSerializer):



    class Meta:
        model = TrubEmail
        # fields = ('rawEmail', 'sender',
        #           )
        fields = '__all__'




class EmailViewSet(viewsets.ModelViewSet):
    queryset = TrubEmail.objects.all()
    serializer_class = EmailSerializer
