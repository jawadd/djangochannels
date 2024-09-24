from django.urls import path
from home import views
urlpatterns = [
    path('<str:group_name>/',views.index ),
]
