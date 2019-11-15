from django.urls import path

from .views import EmployeeView

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('employee/<int:pk>', EmployeeView.as_view()),
    path('employee/', EmployeeView.as_view()),
]