# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import  MeasurementSerializer, SensorSerializer
from rest_framework.response import Response
from django.http import HttpRequest, HttpResponse
import ast

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    # def post(self, request):
    #     name = ast.literal_eval((request.body).decode("utf-8")).get('name')
    #     description = ast.literal_eval((request.body).decode("utf-8")).get('description')
    #     Sensor(name = name, description = description).save()
    #     return Response({'status': 'OK'})

class SensorViewUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

