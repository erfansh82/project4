# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response

# from .serializers import CreateSignalSerializer,ForexSignalSerializer,CryptoSignalSerializer
# from .models import CryptoSignal,ForexSignal,CreateSignal


# # all_signal_list

# class AllSignal(APIView):
#     def get(self,request):
#         query=CreateSignal.objects.all().order_by('id')
#         ser_data=CreateSignalSerializer(query,many=True)
#         return Response(ser_data.data,status=status.HTTP_200_OK)


# # just Crypto Signal list

# class AllCryptoSignal(APIView):
#     def get(self,request):
#         query=CryptoSignal.objects.all().order_by('id')
#         ser_data=CryptoSignalSerializer(query,many=True)
#         return Response(ser_data.data,status=status.HTTP_200_OK)
    

# # just Forex Signal list

# class AllForexSignal(APIView):
#     def get(self,request):
#         query=ForexSignal.objects.all().order_by('id')
#         ser_data=ForexSignalSerializer(query,many=True)
#         return Response(ser_data.data,status=status.HTTP_200_OK)
