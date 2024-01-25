from django.urls import path
from .views import CreateUserView,RetrieveUserView
urlpatterns = [
    path('user/', CreateUserView.as_view(), name="create_user"),
    path('user/<str:username>/', RetrieveUserView.as_view(), name="rUser"),
]
