from restApi.models import banks, branches
from rest_framework import serializers


class BanksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = banks
        fields = ['url', 'id', 'name']


class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = branches
        fields = ['url', 'ifsc', 'branch', 'address',
                  'city', 'district', 'state', 'bank', ]
