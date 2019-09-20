
from django.urls import path
from rest_framework.authtoken import views
from auth_token.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users/', TestView.as_view()),
    path('gettoken/', views.obtain_auth_token),
]