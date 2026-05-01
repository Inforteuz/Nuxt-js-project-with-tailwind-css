from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GeneralInfo
from .serializers import GeneralInfoSerializer

class GeneralInfoAPIView(APIView):
    def get(self, request):
        info = GeneralInfo.objects.first()
        if info:
            serializer = GeneralInfoSerializer(info)
            return Response(serializer.data)
        return Response({})
