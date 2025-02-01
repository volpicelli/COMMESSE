from django.urls import path
from .views import IndexHome,Login,Authenticate,SelectAzienda,GetCantieri


urlpatterns = [
        
        path(r'',IndexHome.as_view()),
        path(r'cantieri',GetCantieri.as_view()),
        #path(r'login',Login.as_view()),
        #path(r'auth',Authenticate.as_view()),
        #path(r'selectazienda/<int:azienda_id>',SelectAzienda.as_view()),
        

]