from django.urls import path
from .views import SensorView, SensorViewUpdate, MeasurementView
urlpatterns = [path('sensors/', SensorView.as_view()),
               path('sensors/<pk>/', SensorViewUpdate.as_view()),
               path('measurements/', MeasurementView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
