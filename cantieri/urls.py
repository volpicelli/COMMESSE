from django.urls import path
from .views import CantiereAdd ,CantiereUpdate,CantiereDetail,GetCantieri,CantieriOrdini,\
        CantieriFatture #,FattureCantiere #IndexHome,Login,Authenticate,SelectAzienda,GetCantieri
from home.models import Cantiere


urlpatterns = [
        
        path(r'add',CantiereAdd.as_view()),
        path(r'update/<pk>',CantiereUpdate.as_view()),
        path(r'<int:cantiere_id>', CantiereDetail.as_view()),
        path(r'<int:cantiere_id>/ordini', CantieriOrdini.as_view()),
        path(r'<int:cantiere_id>/fatture', CantieriFatture.as_view()),
        path(r'list', GetCantieri.as_view()),

        
        

]