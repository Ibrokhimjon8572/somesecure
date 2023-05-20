from django.urls import path
from . import views
urlpatterns = [
    path('postdata/', views.GetTokenForUser.as_view()),
]