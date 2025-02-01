from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework import generics
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions

from .assegnato_cantiere_serializer import Assegnato_CantiereSerializer

from home.models import Personale,Assegnato_Cantiere

import json
from django.conf import settings


class Remove_Lavoratore_Cantiere(APIView):
    def get(self,request,pk):
        Assegnato_Cantiere.objects.get(pk=pk).delete()
        return Response({'Deleted':True})
class Assegnato_CantiereList(generics.ListCreateAPIView):
    queryset = Assegnato_Cantiere.objects.all()
    serializer_class = Assegnato_CantiereSerializer
    cognome = ""
    cantiere = ""

    def post(self, request, *args, **kwargs):
        personale = request.POST['personale']
        cantiere = request.POST['cantiere']
        ore_lavorate = request.POST['ore_lavorate']
        p = Personale.objects.get(pk=personale)
        #c = Cantiere.objects.get(pk=cantiere)
        self.cognome  = p.cognome
        self.cantiere = cantiere
        return self.create(request, *args, **kwargs)

    def handle_exception(self, exc):
        """
        Handle any exception that occurs, by returning an appropriate response,
        or re-raising the error.
        """
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            # WWW-Authenticate header for 401 responses, else coerce to 403
            auth_header = self.get_authenticate_header(self.request)

            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN

        exception_handler = self.get_exception_handler()

        context = self.get_exception_handler_context()
        #context="POLLO"
        response = exception_handler(exc, context)

        if response is None:
            self.raise_uncaught_exception(exc)

        response.exception = True
        response.data.pop('non_field_errors')
        response.data["warning"]="Personale {} gia assegnato al cantiere {}".format(self.cognome.upper(),self.cantiere)
        return response


class Assegnato_CantiereDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assegnato_Cantiere.objects.all()
    serializer_class = Assegnato_CantiereSerializer
    
    def destroy(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Assegnato_Cantiere.objects.get(pk=pk).delete() #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response({'Msg':'OK '+str(pk) +' deleted'})

    def retrieve(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Assegnato_Cantiere.objects.get(pk=pk) #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response(serializer.data)
