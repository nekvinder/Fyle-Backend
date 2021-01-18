from restApi.models import banks, branches
from rest_framework import viewsets
from .serializers import BanksSerializer, BranchesSerializer


class BanksViewSet(viewsets.ModelViewSet):
    queryset = banks.objects.all()
    serializer_class = BanksSerializer


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = branches.objects.all()
    serializer_class = BranchesSerializer
