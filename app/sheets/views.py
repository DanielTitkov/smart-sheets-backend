from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sheet, Blueprint, Data
from .serializers import SheetSerializer, BlueprintSerializer, DataSerializer

# class SheetView(viewsets.ModelViewSet):
#     queryset = Sheet.objects.all()
#     serializer_class = SheetSerializer



class BlueprintView(viewsets.ModelViewSet):
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer



class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class SheetView(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class SheetList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        # sheets = Sheet.objects.filter(user=user)
        sheets = Sheet.objects.all() # temporary
        serializer = SheetSerializer(sheets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = self.request.user
        # data_serializer = DataNestedSerializer(data=request.data) # request data
        sheet_serializer = SheetSerializer(data=request.data, context={'request': self.request})
        print(request.data)
        if sheet_serializer.is_valid():
            data = sheet_serializer.data # field "data" contents
            print("VALID", data)
            return Response({})
        print(sheet_serializer.errors)
        return Response(sheet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def post(self, request, format=None):
    #     user = self.request.user
    #     request_serializer = ResultRequestSerializer(data=request.data)
    #     if request_serializer.is_valid(): # check if result is present 
    #         inventory_id = request_serializer.data.get("inventory")
    #         present_results = Result.objects.filter(user=user, inventory=inventory_id)
    #         if present_results.exists(): # if present - return
    #             result_serializer = ResultSerializer(present_results, many=True)
    #             return Response(result_serializer.data, status=status.HTTP_200_OK)
    #         else: # if not present - create and return
    #             inventory = Inventory.objects.filter(pk=inventory_id).first()
    #             scales = inventory.scales.all() # get all scales for the test
    #             new_results = [s.calculate_result(user=user, inventory=inventory_id) for s in scales]
    #             result_serializer = ResultSerializer(new_results, many=True)
    #             progress = Progress(
    #                 user=user, 
    #                 inventory=Inventory(pk=inventory_id),
    #                 status="DONE",   
    #             )
    #             progress.save()
    #             return Response(result_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)