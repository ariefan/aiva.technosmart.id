from django.urls import path
from .views import welcome, BMICalculatorView

urlpatterns = [
    path('', welcome, name='welcome'),
    path('api/calculate-bmi/', BMICalculatorView.as_view(), name='calculate-bmi'),
]