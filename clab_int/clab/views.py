from django.shortcuts import render
from rest_framework.views import APIView
from .models import*
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.http import  JsonResponse
# Create your views here.
class Datascience(APIView):
    def get(self,request):
        item = Account.objects.all()
        serializer =clabserializer(item,many=True)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data})
    
    def post(self,request):
        serializer = clabserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status": status.HTTP_201_CREATED, "data": serializer.data})
    
    def put(self,request,account_name=None):
        item = Account.objects.filter(account_name =account_name).first()
        serializer =clabserializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status": status.HTTP_200_OK, "data": serializer.data})
    
    def delete(self, request,account_name):
      
         # filter data with respect to project id and delete 
        Account.objects.filter(account_name=account_name).delete()
        return Response({"status": status.HTTP_200_OK})
class Destination(APIView):
    def get(self,request, account_id=None):
        destinations = Account.objects.filter(account_id=account_id)
        data = [{'id': dest.id, 'account_name': dest.account_name} for dest in destinations]
        return JsonResponse(data, safe=False)
    


class IncomingDataAPIView(APIView):
    def post(self, request):
        # Validate data and process accordingly
        if request.content_type != 'application/json':
            return JsonResponse({'message': 'Invalid Data'}, status=400)

        app_secret_token = request.POST.get('app_secret_token')
        if not app_secret_token:
            return JsonResponse({'message': 'Unauthenticated'}, status=401)

        # Process the valid data and send it to the account's destinations
        # Identify the account using the app_secret_token and retrieve its destinations
        # Send the data to the destinations

        return JsonResponse({'message': 'Data received and processed'})
