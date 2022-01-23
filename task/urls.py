from django.urls import path,include
from .views import Create,Change,UserApi
from rest_framework.authtoken import views
from rest_framework import routers

route = routers.DefaultRouter()
route.register('user',UserApi)

urlpatterns = [
    path("",Create.as_view()),
    path("<int:pk>",Change.as_view()),
    path("api/",include(route.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),   
]

