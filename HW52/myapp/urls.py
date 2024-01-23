from django.urls import path
from .views import HelloWorld, GreetUser, MetaController

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello-world'),
    path('greet/<str:username>/', GreetUser.as_view(), name='greet-user'),
    path('meta/', MetaController.as_view(), name='meta-controller'),
]