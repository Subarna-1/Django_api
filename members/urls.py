'''
from django.urls import include, path
from rest_framework import routers
from .views import ClientViewSet, ArtistViewSet, WorkViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
'''

from django.urls import path
from .views import work_list, register

urlpatterns = [
    path('api/works', work_list),
    path('api/register', register),
    path('members/', views.members, name='members'),
]


