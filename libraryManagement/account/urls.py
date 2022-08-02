from django.urls import path
from .views import createViewAccount, editDeleteAccount

urlpatterns = [
    path('createAccount/', createViewAccount.as_view()),
    path('updateAccount/<int:pk>/', editDeleteAccount.as_view()),
]