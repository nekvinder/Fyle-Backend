from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from restApi.models import banks, branches
from rest_framework import viewsets
from .serializers import BanksSerializer, BranchesSerializer


class BanksViewSet(viewsets.ModelViewSet):
    queryset = banks.objects.all()
    serializer_class = BanksSerializer


class BranchesAutoCompleteViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all().order_by("ifsc")
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^branch']


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all().order_by("ifsc")
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^ifsc', '^branch', '^address',
                     '^city', '^district', '^state', ]
