from django.urls import path
from .views import FattureAdd,FattureDetail,FattureList
from home.models import Fatture


urlpatterns = [
        
        path(r'list',FattureList.as_view()),
        path(r'add',FattureAdd.as_view()),
        path(r'<int:fattura_id>', FattureDetail.as_view()),

        #path(r'/update/<pk>',CantiereUpdate.as_view()),

        
        

]
