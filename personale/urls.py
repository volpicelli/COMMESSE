from django.urls import path
from .views import PersonaleAdd,PersonaleDetail,PersonaleList
from home.models import Cantiere


urlpatterns = [
        
        path(r'list',PersonaleList.as_view()),
        path(r'add',PersonaleAdd.as_view()),
        path(r'<int:personale_id>', PersonaleDetail.as_view()),

        #path(r'/update/<pk>',CantiereUpdate.as_view()),

        
        

]
