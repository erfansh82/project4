from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import ActivePlan,CreatePlan
from .serializers import ActivePlanSerializer,CreatePlanSerializer

# api for list of plans
class PlanList(APIView):
    def get(self,request):
        query=CreatePlan.objects.all().order_by('id')
        ser_data=CreatePlanSerializer(query,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)


# api for create plan
class CreatePlanView(APIView):
    def post(self,request):
        ser_data=CreatePlanSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# api for edit plan
class EditPlanView(APIView):
    def put(self,request,pk):
        query=CreatePlan.objects.get(pk=pk)
        ser_data=CreatePlanSerializer(query,data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

# api for hide plan
class HidePlanView(APIView):
    def get(self,request):
        query=CreatePlan.objects.filter(status='hide')
        ser_data=CreatePlanSerializer(query,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)
    

# api for show plan
class ShowPlanView(APIView):
    def get(self,request):
        query=CreatePlan.objects.filter(status='show')
        ser_data=CreatePlanSerializer(query,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)
    
# api for delete plan
class DeletePlanView(APIView):
    def get(self,request,pk):
        query=CreatePlan.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    