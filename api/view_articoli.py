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

from .articoli_serializer import Articoliserializer
from home.models import Articoli,Ordine
import json
from django.db.models import Sum
from django.conf import settings
class ArticoliList(generics.ListCreateAPIView):
    queryset = Articoli.objects.all()
    serializer_class = Articoliserializer

class ArticoliDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articoli.objects.all()
    serializer_class = Articoliserializer
    
    def destroy(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Articoli.objects.get(pk=pk).delete() #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response({'Msg':'OK '+str(pk) +' deleted'})

    def retrieve(self, request, pk,*args, **kwargs):
        #pk = self.kwargs.get('pk')
        object = Articoli.objects.get(pk=pk) #kwargs['pk'])
        serializer = self.serializer_class(object)
        return Response(serializer.data)
    
class ArticoliOrdine(APIView):
    serializer_class = Articoliserializer

    def get(self,request,id_ordine):
        o = Ordine.objects.get(pk=id_ordine)
        a = o.ordine_articoli.all()
        serializer = self.serializer_class(a,many=True)
        return Response(serializer.data)


class GroupArticoli(APIView):
    def get(self,request):
        articoli = Articoli.objects.values('descrizione').annotate(totale=Sum('importo_totale'),quantita=Sum('quantita'))
        res=[]
        for one in articoli:
            a={}
            a['descrizione']=one['descrizione']
            a['totale'] = one['totale']
            a['quantita'] = one['quantita']
            res.append(a)

        return Response(res  )