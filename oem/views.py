from django.shortcuts import render
from rest_framework import generics
from oem.models import OemDetail
from oem.serializers import OemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views
from oem.oemutil import OemService
from oem.oemutil import ExternalResourceCallService

# Create your views here.

externalCallServiceInstance = ExternalResourceCallService


class OemViewListAll(generics.ListCreateAPIView):
    queryset = OemDetail.objects.all()
    serializer_class = OemSerializer

    def delete(self, request, *args, **kwargs):
        queryset = OemDetail.objects.all().delete()
        serializer_class = OemSerializer
        return Response(status=status.HTTP_200_OK)


class OemRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OemDetail.objects.all()
    serializer_class = OemSerializer
    lookup_field = "pk"


class OemGetByIdOrAll(views.APIView):

    def get(self, request, manufacturer, **kwargs):

        """ testing a method call from another class"""
        """ create object of class and call method using that object"""
        oemServiceInstance = OemService
        x = oemServiceInstance.testmethod(oemServiceInstance)
        print("received message from main class ", x)

        y = oemServiceInstance.OemCustomClazz().customMethod()
        print("received message from custom class ", y)

        oemServiceInstance.testMethodWithParams(oemServiceInstance, 1, 2, 3)
        oemServiceInstance.testMethodWithKwArgs(first="first", second="second")

        """ API call to load resource from other microservice """
        """externalCallServiceInstance = ExternalResourceCallService - moved this to global"""
        externalCallServiceInstance.getUsersData()

        if manufacturer:
            oem = OemDetail.objects.filter(manufacturer=manufacturer)

        else:
            oem = OemDetail.objects.all()

        serializer = OemSerializer(oem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserData(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            extenalServiceCall = ExternalResourceCallService
            response = extenalServiceCall.getUsersData()
            return Response(response.json(), status=status.HTTP_200_OK)
        except:
            print('exception occured calling external api')


class BooksInfo(views.APIView):

    def get(self, request, *args, **kwargs):
        """externalservice = ExternalResourceCallService  - access this from global variable"""
        response = externalCallServiceInstance.getBooksData()
        return Response(response, status=status.HTTP_200_OK)


class CreateBook(views.APIView):

    def post(self, request, *args, **kwargs):
        response = externalCallServiceInstance.postBookInfo(request)
        return Response(response, status=status.HTTP_201_CREATED)
