from django.urls import path

from ESCEQ.login.views import LoginESCEQView, LogoutView

urlpatterns = [
    path('', LoginESCEQView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
