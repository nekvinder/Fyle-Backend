from .models import banks, branches
from rest_framework import serializers


class BanksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = banks
        fields = ['url', 'id', 'name']


class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = branches
        fields = ['url', 'ifsc', 'branch', 'address',
                  'city', 'district', 'state', 'bank', ]
