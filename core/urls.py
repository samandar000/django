from django.urls import path
from api.views import get_users, add_user
from django.contrib import admin



urlpatterns = [
    path('user/<int:pk>', get_users),
    path('admin/',admin.site.urls),
    path('add_user',add_user)
]
