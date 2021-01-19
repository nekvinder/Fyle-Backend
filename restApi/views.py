from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import banks, branches
from rest_framework import viewsets
from .serializers import BanksSerializer, BranchesSerializer


class BanksViewSet(viewsets.ModelViewSet):
    queryset = banks.objects.all()
    serializer_class = BanksSerializer


class BranchesAutoCompleteViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all().order_by("ifsc")
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['^branch']


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all().order_by("ifsc")
    serializer_class = BranchesSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filter_fields = ["city"]
    filterset_fields = ["city"]
    search_fields = ['^ifsc', '^branch', '^address',
                     '^city', '^district', '^state', ]
