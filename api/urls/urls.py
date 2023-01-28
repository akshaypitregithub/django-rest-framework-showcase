from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter

from api.views import PersonViewSet, PersonModelViewSet

router = DefaultRouter()
router.register(r'persons-viewset', PersonViewSet, basename='person-viewset')
router.register(r'persons-model-viewset', PersonModelViewSet, basename='person-model-viewset')

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons-drf/', views.person_drf_list),
    path('persons-drf/<int:pk>/', views.person_drf_detail),
    path('persons-class/', views.PersonList.as_view()),
    path('persons-class/<int:pk>/', views.PersonDetail.as_view()),
    path('persons-mixin-class/', views.PersonMixinList.as_view()),
    path('persons-mixin-class/<int:pk>/', views.PersonMixinDetail.as_view()),
    path('persons-generic-class/', views.PersonGenericList.as_view()),
    path('persons-generic-class/<int:pk>/', views.PersonGenericDetail.as_view()),
]

urlpatterns = urlpatterns + router.urls
