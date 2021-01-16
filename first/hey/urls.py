from django.conf.urls import url,include

from hey import views
from rest_framework import routers
from .api import StudentViewSet

router = routers.DefaultRouter()
router.register(r'api/student',StudentViewSet)


urlpatterns = [
    url(r'hello/', views.hello, name='hello'),
    url(r'slist/', views.retrieve, name='slist'),
    url(r'slist_api/', views.retrieve_api, name='slist_api'),
    url(r'elastic_insert/', views.elastic_insert, name='elastic_insert'),
    url(r'^', include(router.urls)),
    
]
