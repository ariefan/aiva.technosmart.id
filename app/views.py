from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from drf_spectacular.utils import OpenApiParameter, extend_schema

def welcome(request):
    return render(request, 'welcome.html')

class BMICalculatorSerializer(serializers.Serializer):
    weight = serializers.FloatField(help_text="Weight in kilograms")
    height = serializers.FloatField(help_text="Height in meters")

@extend_schema(
    methods=['GET'],
    parameters=[
        OpenApiParameter('weight', type=float, description='Weight in kilograms'),
        OpenApiParameter('height', type=float, description='Height in meters'),
    ],
    responses={200: str}
)
class BMICalculatorView(APIView):
    """
    API View for calculating Body Mass Index (BMI).
    """

    def get(self, request):
        weight = request.query_params.get('weight')
        height = request.query_params.get('height')

        if weight is None or height is None:
            return Response({"error": "Please provide weight and height."}, status=status.HTTP_400_BAD_REQUEST)

        weight = float(weight)
        height = float(height)

        # Calculate BMI
        bmi = weight / (height ** 2)
        return Response({'bmi': bmi}, status=status.HTTP_200_OK)
