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
from .cantiere_serializer import Cantiereserializer
from .ordine_serializer import Ordineserializer
from .fatture_serializer import Fattureserializer
from home.models import Cantiere,Azienda,Cliente,Fatture
import json
from django.conf import settings

   
class CantieriAzienda(APIView):
    serializer_class = Cantiereserializer

    #def get(self,request,id_cliente,id_azienda):
    def get(self,request,azienda_id):
        #azienda=Azienda.objects.get(current=True)

        clienti=Cliente.objects.filter(azienda_id=azienda_id)
        tutticantieri = []
        for one in clienti:
            try:
                cantiere = Cantiere.objects.filter(cliente=one)
                for o in cantiere:
                    tutticantieri.append(o)
            except ObjectDoesNotExist:
                pass


        serializer = self.serializer_class(tutticantieri,many=True)
        return Response(serializer.data)

class CantiereList(generics.ListCreateAPIView):
    #azienda=Azienda.objects.get(current=True)
    queryset = Cantiere.objects.all()
    serializer_class = Cantiereserializer



class CantiereDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cantiere.objects.all()
    serializer_class = Cantiereserializer
    
    def destroy(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Cantiere.objects.get(pk=pk).delete() #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response({'Msg':'OK '+str(pk) +' deleted'})

    def retrieve(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Cantiere.objects.get(pk=pk) #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response(serializer.data)
    
class OrdiniCantiere(APIView):
    serializer_class = Ordineserializer

    def get(self,request,id_cantiere):
        c = Cantiere.objects.get(pk=id_cantiere)
        o = c.cantiere_ordine.all()
        serializer = self.serializer_class(o,many=True)

        return Response(serializer.data)
    

class FattureCantiere(APIView):
    serializer_class = Fattureserializer

    def get(self,request,id_cantiere):
        c = Cantiere.objects.get(pk=id_cantiere)
        ordini = c.cantiere_ordine.all()
        resp=[]
        for ordine in ordini:

            fatture = ordine.ordine_fatture.all()
            #for fattura in fatture:
            if fatture:
                serializer = self.serializer_class(fatture,many=True)
                #serializer.data['cantiere'] = id_cantiere
                #serializer.data['ordine'] = ordine.id
                altro = {'fattura':serializer.data, 'cantiere': id_cantiere,'ordine': ordine.id}
                
                resp.append(altro)

        return Response(resp)
