from django.urls import path
from .views import home, login_view

urlpatterns = [
    path('', home, name='home'),               # /user/
    path('login/', login_view, name='login'),  # /user/login/
]
