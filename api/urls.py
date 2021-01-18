from restApi.views import BanksViewSet, BranchesAutoCompleteViewSet, BranchesViewSet
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'banks', BanksViewSet)
router.register(r'branches/autcomplete', BranchesAutoCompleteViewSet)
router.register(r'branches', BranchesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
